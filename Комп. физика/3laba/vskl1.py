import matplotlib.pyplot as plt
import numpy as np
#указываю промежуток графика, количество точек на графике
x = np.linspace(-3, 3, 300)
y = (x**2)*np.exp(-x**2) #первая функция
y2 = x*np.exp(-x**2)
#вторая функция
#указываю то, что и как должно отображаться на графике
plt.plot(x, y, 'c-*', linewidth=2, markersize=5, markerfacecolor='y', color='yellow')
plt.plot(x, y2, 'c-*', linewidth=2, markersize=5, markerfacecolor='g', color='pink')
plt.show()
# -*- coding: utf-8 -*-
