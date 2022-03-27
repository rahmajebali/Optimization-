#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 18:54:40 2022

@author: rahmajebali
"""


import pyomo.environ as pyo
from pyomo.opt import SolverFactory


model = pyo.ConcreteModel()
#Parameters and sets
model.T = pyo.Param(initialize=10)

model.M = pyo.Param(initialize=4)


model.LimitProd = pyo.Param(initialize=10)

model.setT = pyo.RangeSet(1,model.T)
model.setM = pyo.RangeSet(1,model.M)


#variables
model.x = pyo.Var(model.setM ,model.setT,within=pyo.Integers)

#obj function
model.obj = pyo.Objective(expr = pyo.summation(model.x),sense=pyo.maximize)

#constraints
def fisrtrule(model,t):
    return  2*model.x[2,t] - 8*model.x[3,t]<=0
def secondrule(model,t):
    return model.x[2,t]-2*model.x[3,t-2]+model.x[4,t]>=1
def thirdrule(model,t):
    return sum(model.x[m,t] for m in model.setM)<=50
def fourthrule(model,t):
    return model.x[1,t]+model.x[2,t-1]+model.x[3,t]+model.x[4,t]<=model.LimitProd
def fifthrule(model,m,t):
    return pyo.inequality(0, model.x[m,t],10)

model.C1 = pyo.Constraint(model.setT, rule = fisrtrule)
model.C2 = pyo.Constraint(range(3,model.T+1), rule = secondrule)
model.C3 = pyo.Constraint(model.setT, rule = thirdrule)
model.C4 = pyo.Constraint(range(2,model.T+1), rule = fourthrule)
model.C5 = pyo.Constraint(model.setM,model.setT, rule = fifthrule)

        

#solve
opt = SolverFactory('gurobi')
results = opt.solve(model, tee=True)
opt.options['MIPgap'] = 0
opt.options['TimeLimit'] = 0

model.pprint()

print(pyo.value(model.obj))
    
