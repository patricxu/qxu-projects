#!/usr/bin/python
# -*- coding:utf-8 -*-

import math
import numpy as np
import pandas as pd

if __name__ == "__main__":
    np.set_printoptions(linewidth=400)
    x = np.arange(10, dtype=float)
    y = (3 * 2 ** x + 4) / 10
    print x
    print y
    data = pd.read_table('Distance.txt', sep='\t', encoding='GBK', thousands=',')
    distance = data.iloc[:, 1].astype(float)
    distance /= distance[2]
    print distance.values

    # learning_rate = 0.01
    # for a in range(1,100):
    #     cur = 0
    #     for i in range(1000):
    #         cur -= learning_rate*(cur**2 - a)
    #     print ' %d的平方根(近似)为：%.8f，真实值是：%.8f' % (a, cur, math.sqrt(a))
