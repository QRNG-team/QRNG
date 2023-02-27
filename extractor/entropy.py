from collections import Counter

import numpy as np


def min_entropy(in_list):
    """
    Calculates the minimum entropy of the data.
    """
    count = Counter(in_list).most_common(1)[0][1]
    pmax = count / len(in_list)
    min_ent = -np.log2(pmax)
    return min_ent


def shannon_entropy(in_list):
    """
    Calculates the Shannon entropy of the data.
    """
    sh_ent = 0
    for n in dict(Counter(in_list)).values():
        p = n / len(in_list)
        sh_ent = sh_ent - np.log2(p) * p
    return sh_ent


def sample_entropy(in_list, m, r):
    """
    Calculates the Sample entropy of the data.
    m: embedding dimension
    r: tolerance
    """

    def _maxdist(x_i, x_j):
        return max([abs(ua - va) for ua, va in zip(x_i, x_j)])

    def _phi(m):
        x = [[in_list[j] for j in range(i, i + m - 1 + 1)] for i in range(N - m + 1)]
        B = [(len([1 for x_j in x if _maxdist(x_i, x_j) <= r]) - 1.0) / (N - m) for x_i in x]
        return (N - m + 1.0) ** (-1) * sum(B)

    N = len(in_list)

    return -np.log(_phi(m + 1) / _phi(m))


def renyi_entropy(in_list, q):
    """
    Calculates the Renyi entropy of the data.
    q: order
    q>=0 and q not = 1
    """
    sum = 0
    for n in dict(Counter(in_list)).values():
        p = n / len(in_list)
        sum = sum + pow(p, q)
    re_ent = np.log2(sum) * (1 / 1 - q)
    return re_ent


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    f = open('test.txt', 'r')
    flist = []
    for i in range(100):
        flist.append(int(f.readline()))
    print(min_entropy(flist))
    print(shannon_entropy(flist))
    print(sample_entropy(flist, 4, 300))
    print(renyi_entropy(flist, 2))
