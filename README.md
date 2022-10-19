# quantum-random-number-generator
## 项目说明

QRNG项目分为分为	

## Toeplitz

用于后处理量子随机数生成的Toeplitz哈希算法

Toeplitz哈希过程从一些大小为n(由量子态测量产生)的原始数据开始，其最小熵为k(其随机性的下限)和一个安全参数ε。例如，如果我们从输入位长8开始，我们的最小熵是6.7，我们可以从每8位的原始数据中提取6.7个随机位，或80%。有了这个信息，我们可以找到输出长度m。然后我们构造一个具有n + m- 1个随机位种子的Toeplitz矩阵，并将这个矩阵与原始数据相乘，得到提取的随机数据。



Toeplitz hashing algorithm for post-processing quantum random number generation

The procedure of Toeplitz hashing starts with some raw data of size n (produced by the measurement of the quantum state) with a min-entropy of k (the lower bound on its randomness) and a security parameter ε. For example, if we start with an input bit-length of 8 and our min-entropy is 6.7, we can extract 6.7 random bits per 8 bits of raw data, or 80%. With this information, we can find the output length, m. We then construct a Toeplitz matrix with an n + m - 1 random-bit seed and multiply this matrix with the raw data to produce the extracted random data.

## packages

matplotlib>=3.3.4
numpy>=1.19.5
scipy>=1.5.4

## **tips**

+ **由于github仓库容量限制，数据等大文件就不放在仓库里了，大家本地维护即可**

