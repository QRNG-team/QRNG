import matplotlib.pyplot as plt
import numpy as np
import random
import ottoeplitz

""" 
Toeplitz Hashing Example
======================

In this example, we generate a large Gaussian input data set. We plot the data before
and after hashing. The data after hashing should be uniform.

"""


def plot_data(data, n):
        """ Bins up data and plots. """
        N, data = ottoeplitz.Toeplitz._calculate_N(data)
        binned_data, bins = np.histogram(data, bins=2**n-1)     
        data_digital = np.digitize(data, bins, right=True)   
        fig, ax = plt.subplots()  
        ax.hist(data_digital,bins=2**n-1, label='Digitized Raw Data')
        plt.xlabel('Random numbers')
        plt.ylabel('Frequency')
        plt.title("Plotting Data Before and After Hashing")
        plt.show()
        return binned_data, data_digital       
    
