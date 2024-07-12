import matplotlib.pyplot as plt
import numpy as np


def sine(v):
    with np.errstate(invalid='ignore'):
        return np.power(v, (2.0 / 3.0)) + 0.9 * ((3.3 - v ** 2) ** (1 / 2)) * np.sin(12.35 * np.pi * v)


x = np.linspace(-4, 4, 100)
y = sine(x)
y_odbicie = sine(-x)

plt.plot(x, y, 'r')
plt.plot(x, y_odbicie, 'r')
plt.xlim(-3, 3)
plt.ylim(-2, 3)
plt.title('Pełne serduszko z wykorzystaniem funkcji sine(x)')
plt.show()
