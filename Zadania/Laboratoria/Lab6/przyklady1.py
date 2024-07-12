import matplotlib.pyplot as plt
import numpy as np

""" Wprowadzenie do pyplot`a """

# Biblioteka matplotlib.pyplot jest zbiorem funkcji, które sprawiają, że matplotlib działa jak MATLAB. Każda funkcja
# pyplot dokonuje jakiejś zmiany w figurze, np.: tworzy figurę, tworzy obszar wykreślania w figurze, wykreśla jakieś
# linie w obszarze wykreślania, dekoruje wykres etykietami, itp. W matplotlib.pyplot różne stany są zachowywane przez
# wywołania funkcji, więc śledzi takie rzeczy jak bieżąca figura i obszar kreślenia, a funkcje kreślenia są kierowane
# do bieżących osi (proszę zauważyć, że "osie" tutaj i w większości miejsc w dokumentacji odnosi się do części osiowej
# figury, a nie ścisłego terminu matematycznego dla więcej niż jednej osi). Generowanie wizualizacji za pomocą pyplot
# jest bardzo szybkie.

plt.plot([1, 2, 3])
plt.xlabel('Etykieta osi X')
plt.ylabel('Etykieta osi Y')
plt.show()

# Dlaczego oś x ma zakres od 0 do 2, a oś y ma zakres od 1 do 3?
# Jeśli podasz pojedynczą listę lub tablicę do wykreślenia, matplotlib zakłada, że jest to sekwencja wartości
# y i automatycznie generuje dla Ciebie wartości x. Ponieważ zakresy Pythona zaczynają się od 0, domyślny wektor
# x ma taką samą długość jak y, ale zaczyna się od 0. Stąd wartości x to [0, 1, 2]. Plot jest uniwersalną funkcją
# i przyjmuje dowolną liczbę argumentów. Aby zrobić, żeby wartości x i y wyświetlały się podane przez nas, należy
# zastosować kod widoczny poniżej.

plt.plot([1, 2, 3], [1, 4, 9])
plt.show()



""" Formatowanie stylu wykresu """

# Dla każdej pary argumentów x, y istnieje opcjonalny trzeci argument, który jest łańcuchem formatu wskazującym
# kolor i typ linii wykresu. Litery i symbole łańcucha formatu pochodzą z MATLABa, i łączy się łańcuch koloru
# z łańcuchem stylu linii. Domyślnym łańcuchem formatu jest 'b-', który jest niebieską linią ciągłą. Na przykład,
# aby wykreślić wcześniejszy wykres używając czerwonych punktów, należy wydać polecenie widoczne poniżej.

plt.plot([1, 2, 3], [1, 4, 9], 'r.')
plt.axis((0, 4, 0, 10))
plt.show()

# Pełna lista stylów linii i łańcuchów formatowych znajduje się w dokumentacji polecenia plot:
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot.

# Funkcja axis w powyższym przykładzie przyjmuje krotkę (xmin, xmax, ymin, ymax) i określa zakresy wartości
# przedstawiane na osiach.

# Gdyby matplotlib był ograniczony do pracy z listami, byłby dość bezużyteczny do przetwarzania liczb. W rzeczywistości
# wszystkie sekwencje są wewnętrznie konwertowane na tablice numpy. Poniższy przykład ilustruje wykreślanie kilku linii
# o różnych stylach formatowania w jednym wywołaniu funkcji przy użyciu tablic.

# Równomiernie próbkowany czas w odstępach 200ms
t = np.arange(0., 5., 0.2)

# Czerwone kreski, Niebieskie kwadraty, Zielone trójkąty
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()

# Rysowanie kilku wykresów w jednym obszarze roboczym może odbywać się przez:
# * wielokrotne użycie funkcji plot.
x = [1, 2, 3]
y = [2, 4, 6]
plt.plot(x, y, 'bo')
plt.plot(x, [value * 3 for value in y], 'go')
plt.show()

y = np.array([[1, 2], [3, 4], [5, 6]])
for col in range(y.shape[1]):
    plt.plot(x, y[:, col])
plt.show()

# * określenie wielu zestawów składających się z współrzędnych [x], y oraz z stringa definiującego kolor i styl linii:
x = [1, 2, 3]
y = [2, 4, 6]
plt.plot(x, y, 'bo', x, [value * 3 for value in y], 'go')
plt.show()

plt.plot(x, [1, 2, 3], 'go-', label='Linia 1', linewidth=4)
plt.plot(x, [1, 4, 9], 'md:', label='Linia 2', markersize=15)
plt.legend()
plt.show()
