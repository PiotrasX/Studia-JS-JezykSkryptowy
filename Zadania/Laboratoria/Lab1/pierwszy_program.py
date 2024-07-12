""" Pierwszy program """

print("Hello world!")

print()
print(2 + 2)
print(5 - 2 + 4)
print((-7 + 2) * (-4))



""" Operatory """

#       Operator numeryczny	               Opis
#       -------------------         -------------------
#       x + y	                    suma x oraz y
#       x - y	                    różnica x oraz y
#       x * y	                    iloczyn x oraz y
#       x / y	                    iloraz x oraz y
#       x // y	                    (zaokrąglony w dół) iloraz x oraz y
#       x % y	                    reszta z dzielenia x / y
#       abs(x)	                    wartość bezwzględna x
#       divmod(x, y)	            para (x // y, x % y)
#       pow(x, y)	                x do potęgi y
#       x ** y	                    x do potęgi y
#       x += y	                    x = x + y
#       x -= y	                    x = x - y
#       x *= y	                    x = x * y
#       x /= y	                    x = x / y

#       Operator porównania	               Opis
#       -------------------         -------------------
#       x != y	                    x różne od y
#       x == y	                    x równe y
#       x > y	                    x większe od y
#       x < y	                    x mniejsze od y
#       x >= y	                    x większe lub równe od y
#       x <= y	                    x mniejsze lub równe od y



""" Operacje na łańcuchach znaków (stringach) """

print()
print('Hello world!')
print("Hello world!")
print('Hello world\'s!')
print("Hello world's!")

print()
a = "Welcome to Python's world!"
print(a[0])
print(a[0:7])



""" Wprowadzanie danych """

print()
napis = input("Wprowadź dane: ")  # Pobieranie danych z konsoli
print("Twoje dane: " + napis)



""" Konwertowanie typów """

print()
print(3)
print(float(3))



""" Zmienne """

print()
x = 7
print(x)
print(x + 3)
print(x)

x = 123
print(x)
x = "To jest napis"
print(x)
print(x + "!")



""" Instrukcja warunkowa IF """

print()
if 10 > 5:
    print("10 jest większe od 5")

number = 15
print("'number' = " + str(number))
if number > 5:
    print("'number' jest większe niz 5")
    if number <= 45:
        print("'number' jest z przedziału (5; 45]")

if number > 25:
    print("Napis z IF")
else:
    print("Napis z ELSE")

number = 12
if number == 5:
    print("Numerem jest 5")
else:
    if number == 10:
        print("Numerem jest 10")
    else:
        print("Numerem nie jest 5 ani 10")

number = 12
if number == 5:
    print("Numerem jest 5")
elif number == 10:
    print("Numerem jest 10")
elif number == 15:
    print("Numerem jest 10")
else:
    print("Numerem nie jest 5, 10 ani 15")



""" Operatory logiczne """

print()
a = True
b = False
print(a and b)

c = True
d = True
print(c and d)

print()
a = True
b = False
print(a or b)

c = False
d = False
print(c or d)

print()
a = True
print(not a)

b = False
print(not b)



""" Priorytet operatorów """

print()
print(False == False or True)
print(False == (False or True))
print((False == False) or True)
# Kod pokazuje, że == ma wyższy priorytet niż 'or'



""" Pętla WHILE """

print()
i = 1
while i <= 5:
    print(i)
    i += 1
print("Koniec pętli!")

print()
i = 1
while 1 == 1:
    print(i)
    i += 1
    if i >= 10:
        print("Przerwanie pętli")
        break
print("Koniec pętli!")

print()
i = 0
while True:
    i += 1
    if i == 2:
        print("Pominięcie 2")
        continue
    if i == 5:
        print("Przerwanie pętli")
        break
    print(i)
print("Koniec pętli!")



""" Listy """

print()
slowa = ["Hello", "world", "!"]
print(slowa[0])
print(slowa[1])
print(slowa[2])

print()
number = 3
mysli = ["string", 0, [1, 2, number], 3.14]
print(mysli[1])
print(mysli[2])
print(mysli[2][2])

print()
cyfry = [7, 7, 7, 7]
print(cyfry)
cyfry[2] = 5
print(cyfry)

print()
cyfry = [1, 2, 3]
print(cyfry + [4, 5, 6])
print(cyfry * 3)

print()
slowa = ["kolumna", "wiersz", "komorka", "komorka"]
print("komorka" in slowa)
print("wiersz" in slowa)
print("tabela" in slowa)
# 'True' jeśli element znajduje się raz lub więcej razy na liście
# 'False' jeśli element nie znajduje się na liście

print()
cyfry = [1, 2, 3]
print(not 4 in cyfry)
print(4 not in cyfry)
print(not 3 in cyfry)
print(3 not in cyfry)



""" Funkcje list """

print()
cyfry = [1, 2]
print(cyfry)
cyfry.append(3)  # Dodanie elementu na końcu listy (jest to metoda)
print(cyfry)
print(len(cyfry))  # Liczba elementów na liście (jest to funkcja)
cyfry.insert(1, 1.5)
print(cyfry)  # Dodanie elementu na konkretny indeks listy (jest to metoda)

print()
litery = ['q', 'w', 'e', 'r', 't', 'y']
print("Indeks 'r': " + str(litery.index('r')))  # Znajduje pierwsze wystąpienie elementu i zwraca jego indeks
# print("Indeks 'a': " + str(litery.index('a'))) - wywoła błąd, bo element nie znajduje się na liście

print()
cyfry = [3, 6, 1, 2, 6, 7, 5, 4, 8, 0, 9, 2]
print("Wartość maks: " + str(max(cyfry)))
print("Wartość min: " + str(min(cyfry)))
print("Ile razy występuje cyfra '6': " + str(cyfry.count(6)))
print(cyfry)
cyfry.remove(6)  # Usunięcie pierwszego wystąpienia danego elementu z listy
print(cyfry)
cyfry.reverse()  # Odwrócenie listy
print(cyfry)
x = cyfry.pop(2)  # Zwraca i usuwa element z danego indeksu z listy
print(x)
print(cyfry)
cyfry.sort()  # Sortowanie listy
print(cyfry)



""" Pętla FOR """

print()
slowa = ["kot", "pies", "zwierze", "prosiak"]
for slowo in slowa:
    print(slowo + "!")

print()
for i in range(5):
    print(i)
