#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 13:55:41 2017

@author: rosky
"""

import numpy as np
x = np.arange(11)
even = x[1::2]
odd = np.delete(x, even)

print('A lsit of odd points ' + repr(odd))
print('A lsit of even points ' + repr(even))
