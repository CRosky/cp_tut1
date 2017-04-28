#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 14:38:58 2017

@author: rosky
"""

import numpy as np

n_datapoint = [10, 30, 100, 300, 1000]

for i in n_datapoint:
    x = np.linspace(0.0, np.pi/2, i)
    odd = x[1:-2:2]
    even = np.delete(x[1:-2], odd)
    y1 = np.cos(even)
    y_even=y1.sum()
    y2 = np.cos(odd)
    y_odd=y2.sum()
    dx = (x[-1]-x[0])/i
      
    integral = dx*( (np.cos(x[0])/6.0) + ((2.0*y_odd)/3.0) + (y_even/3.0) + (np.cos(x[-1])/6.0) )
    error = 1-integral
    print('for ' + repr(i) + ' number of points, the integral is ' + repr(integral) + ' and error is ' + repr(error))
    
    
## The error decreases as the number of point increases

## We would need a lot of points in Simpson as for 10 point on simple simple sum the corresponding error is 0.023745975047701817. Whereas using Simpson's rule the resulting error is 0.42770379970487937
