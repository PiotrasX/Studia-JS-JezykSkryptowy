import matplotlib.pyplot as plt
import numpy as np

dane = [(100, 90), (110, 95), (120, 105), (130, 110)]
lata = ['Rok 2020', 'Rok 2021', 'Rok 2022', 'Rok 2023']

chlopcy = [d[0] for d in dane]
dziewczeta = [d[1] for d in dane]

x = np.arange(len(lata))
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, chlopcy, width, label='Chłopcy', color='tab:blue')
rects2 = ax.bar(x + width/2, dziewczeta, width, label='Dziewczęta', color='tab:orange')

ax.set_xlabel('Rok')
ax.set_ylabel('Liczba urodzonych dzieci')
ax.set_title('Liczba urodzonych dzieci według płci w danym roku')
ax.set_xticks(x)
ax.set_xticklabels(lata)
ax.legend()
plt.show()
