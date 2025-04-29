from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 100)
y = x**2

plt.plot(x, y, label='y = x^2', color='r')
plt.title('Wykres funkcji y = x^2')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()
