# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 18:09:14 2022
задание: Постройте график функции 𝑓(𝑥)=sin⁡𝑥 в интервале 
[0, 40𝜋]. Постройте график еще раз, растянув его (увеличьте 
отношение ширина/высота).

@author: valeria
"""

import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,40*np.pi,150)
y=np.sin(x)
plt.axes().set_aspect(50)
plt.plot(x,y)
plt.show()