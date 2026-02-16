import matplotlib.pyplot as plt
import numpy as np

""" Praca z wieloma figurami i osiami """

# MATLAB oraz pyplot, umożliwiają wykorzystanie bieżącego obszaru roboczego do rysowania wykresów względem osi
# (jeden pod drugim lub obok drugiego). Wszystkie funkcje kreślenia odnoszą się do bieżących osi. Funkcja gca zwraca
# bieżące osie (instancja matplotlib.axes.Axes), a gcf zwraca bieżącą figurę (instancja matplotlib.figure.Figure).
# Normalnie nie musisz się tym przejmować, ponieważ wszystko jest załatwiane w tle. Poniżej znajduje się skrypt
# tworzący dwa podwykresy.


def f(t):
    return np.exp(t) * np.cos(2 * np.pi * t)


t1 = np.arange(0.0, 5.0, 0.15)
t2 = np.arange(0.0, 5.0, 0.01)

plt.figure()
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2 * np.pi * t2), 'r--')
plt.show()

# Wywołanie funkcji figure jest opcjonalne, ponieważ figura zostanie utworzona, jeśli nie istnieje, tak samo jak oś
# zostanie utworzona (odpowiednik jawnego wywołania subplot()), jeśli nie istnieje. Wywołanie subplot określa numrows,
# numcols, plot_number, gdzie plot_number mieści się w zakresie od 1 do numrows*numcols. Przecinki w wywołaniu subplot
# są opcjonalne, jeśli numrows*numcols<10. Zatem subplot(211) da taki sam rezultat jak subplot(2, 1, 1). Możesz stworzyć
# dowolną liczbę podwykresów i osi. Jeśli chcesz umieścić oś ręcznie, tj. nie na siatce prostokątnej, użyj axes, który
# pozwala określić położenie jako axes([left, bottom, width, height]), gdzie wszystkie wartości są we współrzędnych
# ułamkowych (0 do 1).



""" Inne typy wykresów """

# Wykres kołowy, w którym plasterki będą uporządkowane i wykreślone w kierunku przeciwnym do ruchu wskazówek zegara.
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # Wyeksponowany tylko drugi plaster (to znaczy "Hogs").
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')  # Równe proporcje zapewniają, że wykres jest rysowany jako okrąg.
plt.show()

# Wykres słupkowy
fig2, ax2 = plt.subplots()
fruits = ['apple', 'blueberry', 'cherry', 'orange']
counts = [40, 100, 30, 55]
bar_labels = ['red', 'blue', '_red', 'orange']
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']
ax2.bar(fruits, counts, label=bar_labels, color=bar_colors)
ax2.set_ylabel('fruit supply')
ax2.set_title('Fruit supply by kind and color')
ax2.legend(title='Fruit color')
plt.show()

# Wykres 3D
ax3 = plt.axes(projection="3d")
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
r = 10
x = r * np.outer(np.cos(u), np.sin(v))
y = r * np.outer(np.sin(u), np.sin(v))
z = r * np.outer(np.ones(np.size(u)), np.cos(v))
ax3.plot_surface(x, y, z, rstride=5, cstride=5, cmap=plt.cm.coolwarm)
plt.show()
