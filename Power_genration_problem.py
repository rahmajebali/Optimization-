#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 10:51:32 2022

#solve a Power Genration problem


"""

import pyomo.environ as pyomo
from pyomo.environ import *
from pyomo.opt import SolverFactory
import pandas as pd

#input 
dataGen = pd.read_excel('inputs.xlsx',sheet_name='gen')
dataLoad = pd.read_excel('inputs.xlsx',sheet_name='load')
#number of the genrators
Ng = len(dataGen)

#model
model = pyo.ConcreteModel()
# range(Ng) : Ng generators
model.Pg = pyo.Var(range(Ng),bounds=(0,None))

Pg=model.Pg

#constraints
#sum of all the generators
pg_sum = sum([Pg[g] for g in dataGen.id])
model.balance = pyo.Constraint(expr = pg_sum == sum(dataLoad.value))

model.cond = pyo.Constraint(expr = Pg[0]+Pg[3]>=dataLoad.value[0] )
 
#Creating a list of constraints
model.limits = pyo.ConstraintList()
for g in dataGen.id:
    model.limits.add(expr=Pg[g]<=dataGen.limit[g])
    
#object function 
cost_sum = sum([Pg[g]*dataGen.cost[g] for g in dataGen.id])
model.obj = pyo.Objective(expr = cost_sum )

#the solver
opt = SolverFactory('gurobi')

results = opt.solve(model)

dataGen['Pg'] = [pyo.value(Pg[g]) for g in dataGen.id]

print(dataGen)




