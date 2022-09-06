# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 21:20:04 2022

1.3
Построить график зависимости силы 𝐹 взаимодействия между двумя точечными зарядами 
от расстояния r между зарядами в интервале 2 ≤r≤ 10 см через каждые 0.5 см. 
Заряды 𝑞_1= 20 нКл и 𝑞_2= 30 нКл.

@author: valeria
"""
import matplotlib.pyplot as plt
from numpy import arange

q1 = 20
q2 = 30

x = []
y = []

for r in arange(2, 10, 0.5):
    F = (q1 * q2)/(r ** 2)
    x.append(r)
    y.append(F)

print('F = ', round(F, 2))

plt.plot(x, y)
plt.show()