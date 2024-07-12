from array import *
from itertools import chain

""" Tablice """

# Przykładowa deklaracja tablicy:
# nazwa_tablicy = array(kod_typu_przechowywanych_danych, [inicjalizacja_wartościami])

#     Parametr (typ przechowywanych danych)	    Opis
#     b	                                        Reprezentuje liczbę całkowitą ze znakiem o rozmiarze 1
#     B	                                        Reprezentuje liczbę całkowitą bez znaku o rozmiarze 1
#     c	                                        Reprezentuje znak wielkości 1 bajtu
#     u     	                                Reprezentuje znak Unicode o rozmiarze 2 bajty
#     h	                                        Reprezentuje liczbę całkowitą ze znakiem o rozmiarze 2 bajty
#     H	                                        Reprezentuje liczbę całkowitą bez znaku o rozmiarze 2 bajty
#     i	                                        Reprezentuje liczbę całkowitą ze znakiem o rozmiarze 2 bajty
#     I	                                        Reprezentuje liczbę całkowitą bez znaku o rozmiarze 2 bajty
#     w	                                        Reprezentuje znak Unicode o wielkości 4 bajty
#     l	                                        Reprezentuje liczbę całkowitą ze znakiem o rozmiarze 4 bajtów
#     L	                                        Reprezentuje liczbę całkowitą bez znaku o wielkości 4 bajty
#     f	                                        Reprezentuje zmiennoprzecinkowy rozmiar 4 bajtów
#     d	                                        Reprezentuje zmiennoprzecinkowy rozmiar 8 bajtów

# Pobieranie elementu z tablicy za pomocą indeksu.
my_array = array('i', [1, 2, 3, 4, 5])
print(my_array[1])
print(my_array[2])
print(my_array[0])
print()

# Wypisanie elementów w tablicy za pomocą pętli for.
for i in my_array:
    print(i)
print()

# Dodawanie elementu do tablicy za pomocą metody 'append'.
my_array.append(6)
my_array.append(7)
print(my_array[5])
print(my_array[6])
print()

# Dodawanie elementu do tablicy na konkretny indeks za pomocą metody 'insert'.
print(my_array[0])
my_array.insert(0, 0)
print(my_array[0])
print()

# Dodanie do tablicy innej tablicy za pomocą metody 'extend'.
print(my_array)
my_extend_array = array("i", [8, 9, 10])
my_array.extend(my_extend_array)
print(my_array)
print()

# Dodanie do tablicy listy za pomocą metody 'fromlist'.
print(my_array)
c = [11, 12, 13]
my_array.fromlist(c)
print(my_array)
print()

# Usuwanie konkretnego elementu z tablicy za pomocą metody 'remove', gdy tego elementu nie ma to program wyrzuci błąd.
print(my_array)
my_array.remove(4)
print(my_array)
print()

# Usuwanie ostatniego elementu z tablicy za pomocą metody 'pop'.
print(my_array)
my_array.pop()
print(my_array)
print()

# Odwracanie tablicy za pomocą metody 'reverse'.
print(my_array)
my_array.reverse()
print(my_array)
print()

# Sprawdzenie, pod jakim adresem mieści się tablica i jaką ma długość.
print(my_array.buffer_info())
print()

# Metoda 'index' zwraca pierwszy indeks wystąpienia danego elementu w tablicy.
my_new_array = array('i', [1, 2, 3, 3, 3, 5, 5])
print(my_new_array)
print("Pierwszy indeks '3':", my_new_array.index(3))
print("Pierwszy indeks '5':", my_new_array.index(5))
print()

# Metoda 'count' zlicza ilość wystąpienia danego elementu w tablicy.
print(my_new_array)
print("Ilość wystąpień '3':", my_new_array.count(3))
print("Ilość wystąpień '5':", my_new_array.count(5))
print()

# Metoda 'tounicode' konwertuje tablicę na łańcuch znaków.
word = "spam"
my_array = array(str('u'), [])
my_array.extend(list(word))
print(my_array)
print(my_array.tounicode())
print()

# Konwersja tablicy do listy odbywa się za pomocą metody 'tolist'.
my_array = array('i', [1, 2, 3, 4, 5])
my_list = my_array.tolist()
print(my_array)
print(my_list)
print()

my_array = array('u', ['s', 'p', 'a', 'm'])
my_array.extend(" egg")
print(my_array)
print(my_array.tounicode())
print()



""" None """

# Obiekt None jest używany do reprezentacji braku wartości, jest on podobny do null'a w innych językach programowania.
# Tak jaki inne puste wartości, jak np.: 0, [], pusty ciąg znaków, null; jest on fałszem, gdy skonwertujemy go na
# wartość logiczną. Obiekt None jest zwracany przez funkcję, gdy bezpośrednio nie zwraca ona niczego konkretnego.

x = None
if x is None:
    print("'x' ma wartość None")
else:
    print("'x' ma inną wartość")


def funkcja(argument=None):
    if argument is None:
        print("Brak podanego argumentu dla wywołania funkcji")
    else:
        print("Argument w wywołaniu funkcji ma podaną wartość:", argument)


funkcja()
funkcja("coś")
print()



""" Słowniki """

# Słowniki są strukturą danych, która służy do mapowania dowolnych kluczy na wartość.
# Słowniki mogą być indeksowane tak samo, jak listy przy użyciu kwadratowych nawiasów zawierających klucz.

# Każdy element w słowniku reprezentowany jest przez parę 'klucz: wartość'
ages = {"Marcelina": 78, "Monika": 20, "Krystyna": 24}
print(ages["Marcelina"])
print(ages["Krystyna"])
print()

# Próba pobrania elementu używając klucza, który nie istnieje w słowniku zwróci błąd 'KeyError'.
# print(ages["Piotr"]) - błąd

# Tylko niezmienne obiekty mogą być używane jako klucze dla słowników, czyli takie, których nie można zmienić.
# Próba użycia zmiennego obiektu do słowa kluczowego powoduje błąd 'TypeError'
# bad_dict = {[1, 2, 3]: "one two three"} - błąd

# Klucze słownika mogą mieć wartości różnych typów.
# Do weryfikacji czy klucz znajduje się już w słowniku można wykorzystać operatory 'in' i 'not in' tak jak dla list.
nums = {1: "one", 2: "two", 3: "three"}
print(1 in nums)
print("three" in nums)
print(4 not in nums)
print()

# Metoda get służy do pobierania elementów ze słownika. W przypadku gdy podany argument (klucz)
# nie zostanie znaleziony w słowniku metoda zwróci obiekt 'None'.

pairs = {"orange": [2, 3, 40], 0: "spam", True: False, None: "True", 2: "apple"}
print(pairs.get("orange"))
print(pairs.get(7))
print(pairs.get(2))
print(pairs.get(True))
print(pairs.get(1235, "not in dictionary"))
print()

# Odczytywanie danych ze słownika za pomocą metody 'get' i pętli 'for'.
for i in pairs:
    print(str(i) + " -> " + str(pairs.get(i)))
print()

# Odczytywanie danych ze słownika za pomocą odpowiedniego klucza i pętli 'for'.
for i in pairs:
    print(i, "->", pairs[i])
print()

# Wypisanie elementów słownika w krótkiej wersji.
print([(key, pairs[key]) for key in pairs])
print()

# Scalanie słowników
fish = {'name': "Nemo", 'hands': "fins", 'special': "gills"}
dog = {'name': "Clifford", 'hands': "paws", 'color': "red"}

# Scalanie słowników: Python 3.5+
fish_dog = {**fish, **dog}
print(fish_dog)

# Scalanie słowników: Python 2.X
# from itertools import chain -> To dajemy na samej górze pliku
fish_dog = dict(chain(fish.items(), dog.items()))
print(fish_dog)
print()

# Konstruktor dict() może być użyty do tworzenia słowników z argumentów będących:
# - kluczem z przypisaną do niego wartością,
# - pojedynczej iteracji par klucz-wartość,
# - pojedynczym słownikiem,
# - pojedynczej iteracji par klucz-wartość i następnie kluczem z przypisaną do niego wartością,
# - pojedynczym słownikiem i następnie kluczem z przypisaną do niego wartością,
print(dict(a=1, b=2, c=3))
print(dict([('a', 1), ('b', 2), ('c', 3)]))
print(dict({'a': 1, 'b': 2, 'c': 3}))
print()
print(dict([('a', 1), ('b', 2)], c=3))
print(dict({'a': 1, 'b': 2}, c=3))
print()



""" Krotka """

# Krotki Tuples są podobne do list z wyjątkiem tego, że nie można ich zmieniać po zadeklarowaniu.
# Tworzy się je z wykorzystaniem nawiasów okrągłych: words = ("spam", "eggs", "sausages").
# Dostęp do elementu uzyskuje się przez indeksowanie.
# Próba podmiany któregoś elementu na inny skutkuje błędem TypeError.
# Krotki podobnie jak słowniki i listy mogą się nawzajem zagnieżdżać.
# Krotki można też tworzyć bez użycia nawiasów oddzielając wartości przecinkami.
# Krotki są szybsze niż listy, lecz nie można zmieniać ich zawartości.
my_tuple = "one", "two", "three"
print(my_tuple[0])
my_tuple = ("one", "two", "three")
print(my_tuple[0])
print()



""" Działania na listach """

# Wycinanie list. Wycinanie można też wykonać na krotkach.
# Pierwszy indeks podany w zakresie wycinka listy jest zawarty w wyniku, ale drugi już nie jest.
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(squares[2:6])
print(squares[3:8])
print(squares[0:1])
print()

# Jeśli pominięto pierwszą liczbę w wycinku listy, uważa się ją za początek listy.
# Jeśli pominięto drugą liczbę w wycinku listy, uważa się, że jest ona końcem.
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(squares[:7])
print(squares[7:])
print()

# Wycinanie może się również odbywać z użyciem trzeciej liczby reprezentującej krok dla pobranych wartości z listy.
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(squares[::2])
print(squares[2:7:3])
print()
# Zastosowanie kroku -1 spowoduje pobranie listy od jej końca

# Wzorce list są użytecznym sposobem szybkiego tworzenia list, których zawartość jest zgodna z prostą regułą.
cubes = [i ** 3 for i in range(6)]
print(cubes)
# Wzorzec listy może również zawierać instrukcję 'if'.
evens = [i ** 2 for i in range(10) if i % 2 == 0]
print(evens)
print()

# Przydatne metody dla łańcuchów znaków:
# 🔹 join -> dołącza listę ciągów do innego ciągu znaków jako separator,
# 🔹 replace -> zamienia jeden wycinek napisu innym,
# 🔹 startswith / endswith -> określa, czy istnieje pod łańcuch odpowiednio na początku i na końcu łańcucha,
# 🔹 lower / upper -> zmienia ciągi znaków odpowiednio na małe i wielkie litery,
# 🔹 split -> działa podobnie do 'join' z pewnym separatorem w liście,
# 🔹 format -> podstawia argumenty w ciągu znaków,

print("-_-".join(["spam", "eggs", "spam"]))
print("Hello me".replace("me", "world"))
print("This is a sentence.".startswith("This"))
print("This is a sentence.".endswith("sentence"))
print("This is a sentence.".lower())
print("This is a sentence.".upper())
print("This is a sentence.".split(" "))
print()

nums = [3, 4, 5]
msg = "Numbers: {0} {1} {2}".format(nums[0], nums[1], nums[2])
print(msg)
print("Point: ({x}, {y})".format(x=2, y=3))
print()



""" 'all' i 'any' """

# Funkcje 'all' i 'any' przyjmują listę, krotkę, ..., jako argument. Zwracają wartość 'True' jeśli odpowiednio
# wszystkie lub który kolwiek z jej argumentów ocenia się jako 'True'.
nums = [55, 44, 33, 22, 11]
if all(i > 5 for i in nums):
    print("Wszystkie liczby są większe od 5")
if any(i % 2 == 0 for i in nums):
    print("Przynajmniej jedna liczba jest parzysta")
print()

all([True, True, True])  # Zwraca True
all([True, False, True])  # Zwraca False
all([])  # Zwraca True, bo nie ma żadnego elementu, który jest False

any([True, False, False])  # Zwraca True
any([False, False, False])  # Zwraca False
any([])  # Zwraca False, bo nie ma żadnego elementu, który jest True



""" 'enumerate' """

# Funkcja 'enumerate' może być użyta do iteracji przez wszystkie wartości i indeksy listy jednocześnie.
list_letters = ['a', 'b', 'c', 'd', 'e']
for iv in enumerate(list_letters):
    print(iv)
print()
for index, value in enumerate(list_letters):
    print(index, "->", value)
