# Toeplitz

ottoeplitz
--------

Toeplitz hashing algorithm for post-processing quantum random number generation

The procedure of Toeplitz hashing starts with some raw data of size n (produced by the measurement of the quantum state) with a min-entropy of k (the lower bound on its randomness) and a security parameter ε. For example, if we start with an input bit-length of 8 and our min-entropy is 6.7, we can extract 6.7 random bits per 8 bits of raw data, or 80%. With this information, we can find the output length, m. We then construct a Toeplitz matrix with an n + m - 1 random-bit seed and multiply this matrix with the raw data to produce the extracted random data. 
