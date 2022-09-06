# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 14:01:12 2022

Построить на одном графике кривые зависимости напряженности 𝐸 электрического поля от расстояния r в интервале 1≤𝑟≤6 см, если поле образовано: 
    а) точечным зарядом 𝑞= 33.3 нКл; 
    б) бесконечно длинной заряженной нити с линейной плотностью заряда 𝑟= 5,01 мкКл/м; 
    в) бесконечно заряженной плоскостью с поверхностной плотностью заряда 𝜎= 75 мкКл/м2

@author: valeria
"""
import matplotlib.pyplot as plt
import math


q = 33.3 * (10 ** (-9))
r_zar = 5.01 * (10 ** (-6))
o = 75 * (10 ** (-6))
e0 = 8.85 * (10 ** (-12))
r = 0.01

massive = []
massive1 = []
massive2 = []
massive3 = []

while r <= 0.06:
    E = (q / (4 * math.pi * e0 * (r ** 2)))
    E1 = (r_zar / (2 * math.pi * e0 * r))
    E2 = (o / (2 * e0))
    massive.append(round(r, 2))
    r += 0.01
    massive1.append(E)
    massive2.append(E1)
    massive3.append(E2)

rslt = [["Точечный заряд", massive1[0], massive1[1], massive1[2], massive1[3], massive1[4]],
              ["Однородно заряженная нить", massive2 [0], massive2 [1], massive2 [2], massive2 [3], massive2 [4]],
              ["Заряженная плоскость", massive3[0], massive3[1], massive3[2], massive3[3], massive3[4]],
              ]
headers = ['Расстояние (r, m)', massive[0], massive[1], massive[2], massive[3], massive[4]]
print(rslt, headers)

plt.plot(massive, massive1, 'rosybrown', linewidth=2, markersize=4, markerfacecolor='r', label='Точечный заряд')
plt.plot(massive, massive2 , 'orangered', linewidth=2, markersize=4, markerfacecolor='b', label='Однородно заряженная нить')
plt.plot(massive, massive3, 'chocolate', linewidth=2, markersize=4, markerfacecolor='g', label='Заряженная плоскость')
plt.title('Напряженность электрического поля E(r)')
plt.legend(loc='best')
plt.grid()
plt.show()