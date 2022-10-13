import subprocess
import os


# commands needed to run NIST tests, general framework, not sure it will work!
os.chdir("/rng/sts-2.1.2/sts-2.1.2")
print(os.getcwd())
os.system('./assess 100000')
os.system('0')
os.system('data/dataforNIST.txt')
os.system('1')
os.system('0')
os.system('30')
os.system('0')
os.chdir('/experiments/AlgorithmTesting')
os.popen('vi finalAnalysisReport.txt')







