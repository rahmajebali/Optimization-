#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 16:03:49 2022

@author: rahmajebali
"""

import pyomo.environ as pyo
from pyomo.environ import *
from pyomo.opt import SolverFactory


model = pyo.ConcreteModel()
T = 10
M = 4
#variables
model.x = pyo.Var(range(1,M+1),range(1,T+1),within=Integers,bounds=(0,10))
x = model.x

#obj function
model.obj = pyo.Objective(expr = sum(x[m,t] for m in range(1,M+1) 
                                     for t in range(1,T+1)),sense=pyo.maximize)
#constraints
model.C1 = pyo.ConstraintList()
for t in range(1,T+1):
    model.C1.add(expr = 2*x[2,t] - 8*x[3,t]<=0)

model.C2 = pyo.ConstraintList()
for t in range(3,T+1):
    model.C2.add(expr = x[2,t]-2*x[3,t-2]+x[4,t]>=1)


model.C3 = pyo.ConstraintList()
for t in range(1,T+1):
    model.C3.add(expr = sum(x[m,t] for m in range(1,M+1))<=50)

model.C4 = pyo.ConstraintList()
for t in range(2,T+1):
    model.C4.add(expr = x[1,t]+x[2,t-1]+x[3,t]+x[4,t]<=10)

model.C5 = pyo.ConstraintList()
for m in range(1,M+1):
    for t in range(1,T+1):
        model.C5.add(expr = x[m,t]<=10)
        model.C5.add(expr = x[m,t]>=0)

#solve
opt = SolverFactory('gurobi')
results = opt.solve(model)

model.pprint()
    


    