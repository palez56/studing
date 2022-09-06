                                                                                                                                                                                                                                                                                                                                                                # -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 19:50:19 2022

Задание: Постройте графики функций 
3. 𝑥=4.4(cos⁡(𝑡)+(cos⁡(1.1𝑡))/1.1),   𝑦=4.4(sin⁡(𝑡)−sin⁡(1.1𝑡)/1.1),   𝑡∈[0;20𝜋]

@author: valeria
"""

import matplotlib.pyplot as plt
import numpy as np
t = np.linspace(0,20*np.pi,300)
x=(4.4)*(np.cos(t)+((np.cos(1.1*t)/1.1)))
y=(4.4)*(np.sin(t)-((np.sin(1.1*t)/1.1)))
plt.plot(x,y, linewidth=4, color='pink',label=r'x функция')
plt.legend(fontsize=9, loc='lower left')
plt.title(r'графаик функции', fontsize=20)
plt.show()