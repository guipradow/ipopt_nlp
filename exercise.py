import pyomo.environ as pyo
from pyomo.opt import SolverFactory

model = pyo.ConcreteModel()

model.x = pyo.Var(bounds=(-5, 5))
model.y = pyo.Var(bounds=(-5, 5))
x = model.x
y = model.y

model.obj = pyo.Objective(expr= pyo.cos(x+1) + pyo.cos(x)*pyo.cos(y),
                          sense=pyo.maximize)

opt = SolverFactory('ipopt', executable='C:/Ipopt/bin/ipopt.exe')
opt.options['tol'] = 1e-6
opt.solve(model)

model.pprint()
print(f'x = {pyo.value(x)}')
print(f'y = {pyo.value(y)}')
