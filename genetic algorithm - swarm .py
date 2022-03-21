#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 18:14:34 2022

@author: rahmajebali
"""

import numpy as np
from pyswarm import pso

#define the objective function 
def model_obj(x):
    pen = 0
    #define x as integer
    x[0]=np.round(x[0],0)
    if not -x[0]+2*x[1]*x[0]<= 8: pen = np.inf
    if not 2*x[0]+x[1]<=14: pen = np.inf
    if not 2*x[0]-x[1]<=10: pen = np.inf
    return - (x[0]+x[1]*x[0]) + pen

#contructing constraints, but in this case we put them in the objective function
def cons(x):
    return[]

#lower bound for x and y 
lb = [0,0]
#upper bound for x and y 
ub = [10,10]

#initial point 
x0 = [0,0]

xopt, fopt = pso(model_obj, lb, ub, x0,cons)

print('x=', xopt[0])
print('y=', xopt[1])