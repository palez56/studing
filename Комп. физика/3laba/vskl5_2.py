# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 19:42:50 2022
Задание: Постройте графики функций 
2. 3. 𝑥=4.4(cos⁡(𝑡)+(cos⁡(1.1𝑡))/1.1),   𝑦=4.4(sin⁡(𝑡)−sin⁡(1.1𝑡)/1.1),   𝑡∈[0;20𝜋]


@author: valeria
"""

import matplotlib.pyplot as plt
import numpy as np
t = np.linspace(-8*np.pi,8*np.pi,10000)
y=np.exp(np.sin(t))-2*np.exp(np.cos(4*t))+(np.sin((2*t-np.pi)/24))**5
plt.polar(t,y, linewidth=4, color='peachpuff')

plt.title(r'графаик функции', fontsize=20)
plt.savefig("MyGraph.png",dpi=200)
plt.show()