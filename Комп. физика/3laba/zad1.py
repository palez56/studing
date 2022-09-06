# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 13:41:15 2022

1. Для введенных пользователем величин зарядов диполя (±𝑄) (в нКл) 
и плеча диполя 𝑙 (в см) определите напряженность 𝐸 электростатического 
поля на продолжении оси электрического диполя в точке A (лекция). 
Постройте график зависимости 𝑬(𝒓).
ε_0= 8.85·〖10〗^(−12)  Ф/м

@author: valeria
"""
import matplotlib.pyplot as plt
import numpy as np
q=float(input("Q="))
l=float(input("l="))
e0=8.95*10**(-12)
x = []
y = []

for r in range(1,20):
    e = (1/(4*np.pi*e0))*2*q*l/(r**3)
    x.append(r)
    y.append(e)
    
print("E = ", e)
plt.plot(x,y, linewidth=4, color='plum')
plt.show()