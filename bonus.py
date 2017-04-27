#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 16:04:32 2017

@author: rosky
"""

import numpy as np
import scipy.integrate as quad


val,err=quad.quad(func_example.mygauss,-20,20)
print val
val,err=quad.quad(func_example.mygauss,-25,15)
print val

#Since integral is the difference between two areas and Gaussian is even on that interval and not even on the second integral interval. Thus different areas between the intervals
#To fix the problem the another area of the upper limit to the posetive lower limit interval must be added

val,err=quad.quad(func_example.mygauss,-25,15) + quad,quad(func_example.mygauss,15,25)
print val
