# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 20:14:47 2022

Задание: Постройте графики функций 
4. 𝑥=6.2(cos⁡(𝑡)−(cos⁡(3.1𝑡))/3.1),  𝑦=6.2(sin⁡(𝑡)−sin⁡(3.1𝑡)/3.1),    𝑡∈[0;20𝜋]


@author: valeria
"""

import matplotlib.pyplot as plt
import numpy as np
t = np.linspace(0,20*np.pi,300)
x=(6.2)*(np.cos(t)-((np.cos(3.1*t)/3.1)))
y=(6.2)*(np.sin(t)-((np.sin(3.1*t)/3.1)))
plt.plot(x,y, linewidth=4, color='plum',label=r'x функция')
plt.legend(fontsize=9, loc='lower left')
plt.title(r'графаик функции', fontsize=20)
plt.show()