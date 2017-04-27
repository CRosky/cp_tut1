#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 15:43:48 2017

@author: rosky
"""

import numpy as np
import matplotlib.pyplot as plt


err_simple=[]
n_datapoint = [10, 30, 100, 300, 1000]
err = []
for i in n_datapoint:
    x = np.linspace(0.0, np.pi/2, i)
    y = np.cos(x)
    total = y.sum()*(x[-1]-x[0])/i
    error = 1-total
    err_simple.append(error)
    print('for ' + repr(i) + ' number of points, the integral is ' + repr(total) + ' and error is ' + repr(error))
    

err = []
for i in n_datapoint:
    x = np.linspace(0.0, np.pi/2, i)
    even = x[1::2]
    odd = np.delete(x, even)
    y1 = np.cos(even)
    y_even=y1.sum()
    y2 = np.cos(odd)
    y_odd=y2.sum()
    dx = (x[-1]-x[0])/i
      
    integral = dx*( (np.cos(x[0])/6.0) + ((2.0*y_odd)/3.0) + (y_even/3.0) + (np.cos(x[-1])/6.0) )
    error = 1-integral
    err.append(error)
    print('for ' + repr(i) + ' number of points, the integral is ' + repr(integral) + ' and error is ' + repr(error))
    
    
print(err_simple)
print(err) 

y_simple=1+np.exp(err_simple)
y_simpson=1+np.exp(err)
plt.plot(n_datapoint,y_simple, 'r-', label='standard sum')
plt.plot(n_datapoint, y_simpson, 'k-', label='Simpson rule')
#get the current figure axes
ax=plt.gca()
#set the yscale to be logarithmic
ax.set_yscale('log')
plt.xlabel('number of points')
plt.ylabel('errors')
plt.legend()
plt.draw()
#let's write the figure to disk
plt.savefig('logplot_example')
