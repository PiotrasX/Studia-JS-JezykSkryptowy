from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label='y = sin(x)', color='r')
plt.plot(x, y2, label='y = cos(x)', color='g')
plt.title('Wykresy funkcji y = sin(x) i y = cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()

plt.xticks([0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi],
           ['0', 'π / 2', 'π', '(3 / 2) * π', '2 * π'])

plt.show()
