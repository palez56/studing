# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 19:09:45 2022
Задание: Постройте графики функций 
1. 𝑟(𝑡)=sin⁡(7/4 𝑡) в интервале [0, 8𝜋];

@author: valeria
"""
import matplotlib.pyplot as plt
import numpy as np
t = np.linspace(0,8*np.pi,10000)
y=np.sin((7/4)*t)
plt.polar(t,y, linewidth=4, color='pink')
plt.title(r'графаики функции r(t)=sint((7/4)*t)', fontsize=20)
plt.show()