import pyomo.environ as pyo, numpy as np
from pyomo.environ import *
from pyomo.opt import SolverFactory



model = pyo.ConcreteModel()

model.N = pyo.Var(within=Integers, bounds=(0,None))
model.p = pyo.Var(bounds=(50,200))
N = model.N
p= model.p


model.C1 = pyo.Constraint(expr= N == 1001 - 5*p)

model.obj = pyo.Objective(expr= p*N, sense=maximize)



opt = SolverFactory('couenne')
opt.solve(model)

model.pprint()

N_value = pyo.value(N)
p_value = pyo.value(p)

print('\n---------------------------------------------------------------------')
print('x=',np.round(N_value))
print('y=',np.round(p_value))
print('revenue = ', np.round(N_value*p_value))