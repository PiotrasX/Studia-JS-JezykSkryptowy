""" Funkcje """


# Deklaracja funkcji
def my_func():
    print("spam")
    print("spam")
    print("spam")


# Wywołanie funkcji
my_func()
print()


# Funkcja przyjmująca argument
# Argumenty funkcji są widoczne tylko w środku danej funkcji
def print_with_exclamation(word):
    print(word + "!")


print_with_exclamation("spam")
print_with_exclamation("eggs")
print_with_exclamation("python")
print()


# Funkcja zwracająca wartość
# Kod, który znajduje się po słowie 'return' nie zostanie wywołany
def maximum(x, y):
    if x >= y:
        return x
    else:
        return y


print(maximum(4, 6))
z = maximum(9, 3)
print(z)
print()


def multiply(x, y):
    return x * y


a = 4
b = 6
# Utworzenie funkcji jako obiektu
operation = multiply
print(operation(a, b))
print()


def add(x, y):
    return x + y


# Funkcja przyjmująca jako argument inną funkcję
def do_twice(func, x, y):
    return func(func(x, y), func(x, y))


a = 5
b = 10
print(do_twice(add, a, b))
print()



""" Błędy """

try:
    var = 100
    var2 = 5 + 3
    print(var / 0)
except ZeroDivisionError:
    print("Błąd dzielenia przez 0")
except (ValueError, TypeError):
    print("Błąd wartości lub typu")

try:
    word_ex = "spam"
    print(word_ex[5])
except:
    print("Wykryto błąd")

try:
    print("hello")
    print(1 / 0)
except ZeroDivisionError:
    print("Błąd dzielenia przez 0")
finally:
    print("Ta linia kodu wykona się zawsze o bloku 'try'")

# raise — Służy do wywołania wyjątku, należy podać typ wyjątku
# raise ValueError
# raise ValueError("Komunikat wyjątku")

# assert — Kontrolują stan po wykonaniu określonego fragmentu kodu, jeśli wynik jest fałszywy, to rzucany jest wyjątek
# assert 2 + 2 == 4
# assert 1 + 1 == 3 -> Tutaj zostanie wyrzucony wyjątek
# assert -3 >= 0, "Mniej niż 0"



""" Operacje na plikach """

# Aby operować na pliku, najpierw trzeba go otworzyć
# Należy pamiętać, że po zakończonej pracy na pliku, taki plik należy zamknąć
myfile = open("spam.txt")
myfile.close()

# Domyślnym trybem otwierania pliku jest "r", czyli tryb tylko do odczytu
# myfile = open("spam.txt", "w") -> Zapewnia tryb zapisu zawartości pliku (nadpisuje wcześniejszą zawartość lub
#                                   tworzy plik, gdy nie istnieje)
# myfile = open("spam.txt", "r") -> Zapewnia możliwość dopisywania do pliku bez utraty wcześniejszej jego zawartości
# myfile = open("spam.txt", "wb") -> Otwiera plik w trybie binarnym używane do plików innych niż tekstowe np.:
#                                    obrazy, dźwięk, itp.

# read() - Bez argumentu odczytuje cały plik, z podanym argumentem odczytuje określoną liczbę bajtów
print()
file = open("spam.txt", "r")
print(file.read(5))
print(file.read(3))
print(file.read())
file.close()

# readline() - Odczytuje każdą linię osobno i zwraca do tablicy
print()
file = open("spam.txt", "r")
print(file.readlines())
file.close()

# Można też odczytać każdą linię za pomocą pętli 'for'
print()
file = open("spam.txt", "r")
for line in file:
    print(line, end="")
file.close()

# Usuwa poprzednią zawartość pliku i zapisuje nową
print()
file = open("save.txt", "w")
file.write("Ten tekst zostanie zapisany do pliku\n")
file.close()

# with — Tworzy tymczasową zmienną, która dostępna jest wyłącznie na poziomie wciętego bloku instrukcji 'with'
#        Automatycznie zamyka plik, nawet jeśli wystąpi jakiś błąd
with open("save.txt") as f:
    print(f.read())
