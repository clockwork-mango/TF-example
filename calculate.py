import numpy as np
from numpy import *

numlist = list(range(11))
numlist.remove(0)

for n in numlist:
    test_all = np.load('data/WT/WT_{0} red.tifperivalues-w.npy'.format(n))
    test_range = []
    test_small = []
    test_big = []
    for i in test_all:
        if 0 < i < 1:
            test_range.append(i)
    for j in test_range:
        if 0 < j < 0.5:
            test_small.append(j)
        else:
            test_big.append(j)
    small_num = len(test_small)
    big_num = len(test_big)
    ratio = big_num/small_num
    range_mean = mean(test_range)
    print('{0} {1} {2}'.format(n,ratio,range_mean))
