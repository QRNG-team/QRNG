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

inputdata = []

# for i in range(2**17):
#     temp = random.gauss(5, .05)
#     inputdata.append(temp)
f = open('../数据/输入2.5mW量程0.1V-混合噪声.txt', 'r')
for i in range(2**16):
        inputdata.append(int(f.readline()))
inputdata = np.array(inputdata)

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
    

t = ottoeplitz.Toeplitz(inputdata, 14)
#plot_data(inputdata, 14)
dist = t.hash()
print(len(dist), len(dist)/len(inputdata))
#plot_data(dist, 14)