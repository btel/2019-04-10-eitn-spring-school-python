#!/usr/bin/env python
#coding=utf-8

import numpy as np
from scipy import io

if __name__ == "__main__":
    #main

    FS = 1250
    mat = io.loadmat('LFPwspk.mat')
    data = mat["Mtx"]
    lfp = data[:10, :FS*5]
    np.savetxt('lfp.txt', lfp.T, delimiter=',', fmt='%.3f')
