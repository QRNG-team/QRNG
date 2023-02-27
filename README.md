# quantum-random-number-generator
## 项目说明

QRNG项目分为分为后提取部分、随机数检测部分（QRNGdetection）、UI、Tool、资源文件（source）和程序文档六部分组成。

UI为基于PyQt5的可视化界面具体实现；后提取部分负责使用Toeplitz-hash方法对原始随机序列进行提取，消除噪声；随机数检测部分（QRNGdetection）负责检测生成的最终序列是否具有真随机数的性质；文档包括软件设计开发的相关文字资料与图，资源文件为图标等文件，Tool中包含跨文件全局变量等工具方法。

主程序入口为mainwindow.py。

具体的实现逻辑详见代码注释。	

## 使用说明
在进行随机数提取时需要先打开原始序列文件并设置好提取结果输出文件位置，才能成功运行提取。在进行随机数检测时需要先打开待检测文件并设置好检测结果输出文件位置，才能成功运行检测。检测时间较长，请耐心等待。

## Toeplitz

用于后处理量子随机数生成的Toeplitz哈希算法

Toeplitz哈希过程从一些大小为n(由量子态测量产生)的原始数据开始，其最小熵为k(其随机性的下限)和一个安全参数ε。例如，如果我们从输入位长8开始，我们的最小熵是6.7，我们可以从每8位的原始数据中提取6.7个随机位，或80%。有了这个信息，我们可以找到输出长度m。然后我们构造一个具有n + m- 1个随机位种子的Toeplitz矩阵，并将这个矩阵与原始数据相乘，得到提取的随机数据。



Toeplitz hashing algorithm for post-processing quantum random number generation

The procedure of Toeplitz hashing starts with some raw data of size n (produced by the measurement of the quantum state) with a min-entropy of k (the lower bound on its randomness) and a security parameter ε. For example, if we start with an input bit-length of 8 and our min-entropy is 6.7, we can extract 6.7 random bits per 8 bits of raw data, or 80%. With this information, we can find the output length, m. We then construct a Toeplitz matrix with an n + m - 1 random-bit seed and multiply this matrix with the raw data to produce the extracted random data.

## packages
PyQt5>=5.15
matplotlib>=3.3.4
numpy>=1.19.5
scipy>=1.5.4


## **tips**

+ **由于github仓库容量限制，数据等大文件就不放在仓库里了，大家本地维护即可**
+ **数据及输出等内容应放到项目的上一级目录的“实验”文件夹，即“实验”与“QRNG”应在同一目录下，“实验”文件内部结构详见代码中定义**
+ **后提取部分的输出提取后序列文件需要在提取后文件路径下创建以实验数据类型为名的文件夹，这样后提取结果、参数和检测结果才会导出。否则报错**

