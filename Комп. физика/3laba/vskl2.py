# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 17:50:05 2022
 Задание: в одном окне постройте графики функций: 
𝑦=2/𝑥, 𝑦1=√𝑥, 𝑦2=−𝑥^2. Отобразите заголовок графика, 
легенду. Сохраните рисунок с графиком в файл. 

@author: valeria
"""

import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-5,5,150)
y1=2/x
y2=np.sqrt(x)
y3 = (-x)**2
plt.plot(x, y1, '-r', linewidth=3, label=r'y=(2/x)')
plt.plot(x, y2, '-b', linewidth=3, label=r'y=sqrt(x)')
plt.plot(x, y3, '-g', linewidth=3, label=r'y=(-x)^2')
plt.legend(fontsize=9, loc='lower left')
plt.title(r'графаики функций', fontsize=20)
plt.savefig("MyGraph.png",dpi=200)
plt.show()