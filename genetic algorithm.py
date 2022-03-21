#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 17:41:17 2022

@author: rahmajebali
"""

import numpy as np
from geneticalgorithm import geneticalgorithm as ga

#define the objective function
#x is an input , - to have a maximization 
#pen is a penelazation in the objective function activated by the constraint
def f(x):
    pen = 0
    if not -x[0]+2*x[1]*x[0]<= 8: pen = np.inf
    if not 2*x[0]+x[1]<=14: pen = np.inf
    if not 2*x[0]-x[1]<=10: pen = np.inf
    return -(x[0]+x[1]*x[0]) + pen



#define bound of the variables
varbound = np.array([[0,10],[0,10]])

#define type of the variables
vartype = np.array([['int'],['real']])

#create the model
model = ga(function = f, dimension = 2, variable_type_mixed=vartype
           , variable_boundaries=varbound)

model.run()
