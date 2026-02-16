import matplotlib.pyplot as plt

dane = [60, 70, 80, 90, 100, 70, 80, 80, 85, 95]

plt.hist(dane, bins=10, edgecolor='black')
plt.title('Rozkład wyników testu u studentów')
plt.xlabel('Wynik testu (%)')
plt.ylabel('Liczba studentów')
plt.show()
