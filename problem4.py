#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 13:55:41 2017

@author: rosky
"""

import numpy as np
even = []
odd = []
x = np.arange(1001)
for i in range(len(x)):
    if x[i]%2 == 0 and i > 0 and i < len(x):
        even.append(x[i])
    elif i > 0 and i < len(x):
        odd.append(x[i])

print('A lsit of odd points ' + repr(odd))
print('A lsit of even points ' + repr(even))
