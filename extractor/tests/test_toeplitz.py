from unittest import TestCase
import pytest
from ottoeplitz import Toeplitz
import numpy as np

file1 = open('test_data.txt', 'r')
data = file1.read()
data = float(data)
np.random.seed(0)

class TestToeplitz:
    n = 8

    def test_calculate_N(self):
        assert Toeplitz._calculate_N(self.data) == 15


    def test_min_entropy(self): 
        assert int(Toeplitz._min_entropy(self)) == 6

    def test_output_length(self, n): 
        assert Toeplitz._output_length(self, n) == 199

    def test_toep_mat(self, n):
        toeplitz_matrix = open("Toeplitz.txt", "r")
        assert Toeplitz._toep_mat(self, n) == toeplitz_matrix
        toeplitz_matrix.close()
    
    def test_decToBin_data(self):
        # toeplitz_matrix = open("Toeplitz.txt", "r")
        # assert Toeplitz._toep_mat(self, n) == toeplitz_matrix
        # toeplitz_matrix.close()
        pass

    def test_hash(self, n):
        pass
