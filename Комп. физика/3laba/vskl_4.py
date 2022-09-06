# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 18:20:29 2022
Задание: на одном рисунке постройте 
графики функций: 
𝑦=𝑒^𝑥, 𝒙=𝑙𝑛 𝑦. 
Сохраните рисунок в отдельный файл. 

@author: valeria
"""

import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 5, 10)
y = np.e**x
fig = plt.figure(facecolor='tan')
ax1 = fig.add_axes([0.1,0.1,0.8,0.8])
ax2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])
ax1.plot(x, y, 'r', linewidth = 3)
ax1.set_title('График функции $e^{x}$')
ax2.plot(y, x, 'orange', linewidth=3)
ax2.set_xlabel('y')
ax2.set_xlabel('x')
ax2.set_title('ln y')
plt.show()