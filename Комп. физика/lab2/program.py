import numpy as np
import matplotlib.pyplot as plt


def f(x, y):
    return (1-x/4 + x**3 + y**3) * np.exp(-x**2 - y**2)*(x**2 - y - x)


t = np.linspace(-3, 3, 121)
X, Y = np.meshgrid(t, t)
Z = f(X, Y)
plt.contourf(X, Y, Z, 16, alpha = 0.9, cmap = 'jet')
plt.contour(X, Y, Z, 16, colors = 'black', linewidth = 0.5)
plt.gcf().set_facecolor('w')
plt.gcf().gca().axis('image')

plt.show()