import matplotlib.pyplot as plt
import numpy as np

ax = plt.axes(projection="3d")
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
x, y = np.meshgrid(x, y)
z = x**2 + y**2

ax.plot_surface(x, y, z, rstride=5, cstride=5, cmap=plt.cm.coolwarm)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Wykres 3D powierzchni z = x^2 + y^2')
plt.show()
