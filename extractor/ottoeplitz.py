"""
ottoeplitz
==========

This module contains the main ``Toeplitz`` class. This is where
the toeplitz hashing takes place.

"""

from typing import Callable
import numpy as np
import pickle
from scipy.constants import *
from scipy.linalg import toeplitz
import Tool.glo as glo


class Toeplitz:
    """ 
    The ``Toeplitz`` class executes the Toeplitz hashing. It 
    requires a large set of random data and the resolution of your
    ADC as input.

    Parameters
    ----------
    data : list
        Input data to be hashed.
    bits : int
        Resolution of your ADC or how many bits you want to represent each random number with.

    Returns
    -------
    hashed_data : list
        Data after Toeplitz hashed.
    """

    def __init__(self, data, bits):
        self.data = data
        self.bits = bits
        self.min_ent = 0

    def _calculate_N(self):
        """ 
        Calculates a power of 2 closest to, but under, the size
        of the original input data. We call this power, N. Resizes 
        data by taking first 2^N data points and deleting the rest.

        Returns
        -------
        N : int
            Power of 2 just under size of input data.
        data : list
            Resized input data.
        """
        N = 0
        while (len(self.data) - 2 ** N) >= 0:
            N += 1
        N -= 1
        indices = []
        for i in range(2 ** N, len(self.data)):
            indices.append(i)
        data = np.delete(self.data, indices)
        return N, data

    def _min_entropy(self):
        """
        Calculates the minimum entropy of the data.

        Returns 
        -------
        min_ent : float
            Minimum entropy of the input data.
        """
        binned_data, bins = np.histogram(self.data, bins=2 ** self.bits - 1)
        N, data = self._calculate_N()
        pmax = np.max(binned_data) / 2 ** N
        min_ent = -np.log2(pmax)
        self.min_ent = min_ent
        # return 0.4 * min_ent
        return min_ent

    def _output_length(self):
        """ 
        Calculates length of the output data using min-entropy.

        Returns 
        -------
        out_len : int
            Length of the output data.
        """
        min_ent = self._min_entropy()
        out_len = 2 ** self.bits * (min_ent / self.bits)
        out_len = round(out_len)
        return out_len

    def _toep_mat(self, data_flat):
        """
        Constructs a random n x m binary Toeplitz matrix.
        
        Returns 
        -------
        toep_mat : 2D array
            A random n x m binary Toeplitz matrix.
        """
        out_len = self._output_length()
        # row = np.random.randint(2, size=out_len)
        # col = np.random.randint(2, size=2**self.bits)
        row = []
        for i in range(out_len):
            row.append(data_flat[self.bits * 2 ** self.bits + i])
        row = np.array(row)
        col = []
        for i in range(2 ** self.bits):
            col.append(data_flat[self.bits * 2 ** self.bits + out_len + i])
        col = np.array(col)
        toep_mat = toeplitz(row, col)
        return toep_mat

    def _dec_num_to_bin(self, data_pt, depth, bin_pts):
        """ 
        General function converting decimal number to binary number.

        Parameters
        ----------
        data_pt : int
            Number you want to convert to binary.
        depth : int
            How many bits you want the number represented with.
        bin_pts : list
            Binary number of size 'bits' converted from decimal. Recursive part of function.
        
        Returns 
        -------
        bin_pts : list
            Binary number of size 'bits' converted from decimal.
        """
        if data_pt >= 1:
            bin_pts = self._dec_num_to_bin(data_pt // 2, depth - 1, bin_pts)
            bin_pts[depth] = data_pt % 2
        return bin_pts

    def _dec_list_to_bin(self):
        """
        Converts data from decimal to binary.

        Returns 
        -------
        bin_data_flat : array
            Data converted from decimal to binary and flattened.
        """
        N, data = self._calculate_N()
        binned_data, bins = np.histogram(self.data, bins=2 ** self.bits - 1)
        data_digital = np.digitize(data, bins, right=True)
        binary_data = []
        for i in range(2 ** N):
            zeros = np.zeros(self.bits)
            # binary_data.append(self._dec_num_to_bin(data[i] + 8192, self.bits - 1, zeros))
            binary_data.append(self._dec_num_to_bin(data_digital[i], self.bits - 1, zeros))
            # print(data_digital[i], self._dec_num_to_bin(data_digital[i], self.bits - 1, zeros))
        binary_data = np.reshape(binary_data, (2 ** N, self.bits))
        bin_data_flat = binary_data.flatten()
        return bin_data_flat

    def hash(self, flag):
        """
        Performs the Toeplitz hashing.

        Returns 
        -------
        hashed_data : array
            Digitized hashed data.
        """
        N, data = self._calculate_N()
        decimal = None
        out_len = self._output_length()
        data_flat = self._dec_list_to_bin()
        toep_mat = self._toep_mat(data_flat)

        split = np.array_split(data_flat, self.bits * 2 ** (N - self.bits))
        data_hashed = np.dot(toep_mat, split[0]) % 2
        for index, data in enumerate(split[1:-1]):
            sample_hashed = np.dot(toep_mat, data) % 2
            data_hashed = np.append(data_hashed, sample_hashed)
            glo.set_value('extractbar', (index / len(split)) * 100)
        # print(type(data_hashed[1]))
        if flag:
            data_hashed_1 = np.array_split(data_hashed, out_len * 2 ** (N - self.bits))
            decimal = []
            for index, sample in enumerate(data_hashed_1):
                x = ''.join([str(int(elem)) for elem in sample])
                decimal = np.append(decimal, int(x, 2))
            # hashed_data = decimal[decimal != 254]
        else:
            pass
        return data_hashed, decimal

# if __name__ == "__main__":
#     time_stamp = "2021_7_6_10_52"
#     z_measur = f"C:/Users/sarah/Box/CamachoLab/Christian/QRNG/data/{time_stamp}_data.p"
#     z_data = pickle.load(open(z_measur, "rb"))
#     data = np.array(z_data["z_powmeas"])[-1]

#     t = Toeplitz(data, 8)
