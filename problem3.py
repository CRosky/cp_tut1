#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 11:14:11 2017

@author: rosky
"""

import numpy as np
import matplotlib.pyplot as plt

n_datapoint = [10, 30, 100, 300, 1000]
err = []
for i in n_datapoint:
    x = np.linspace(0.0, np.pi/2, i)
    y = np.cos(x)
    total = y.sum()*(x[-1]-x[0])/i
    error = 1-total
    print('for ' + repr(i) + ' number of points, the integral is ' + repr(total) + ' and error is ' + repr(error)) 