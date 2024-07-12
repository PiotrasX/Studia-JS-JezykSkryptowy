import math


def zapis_do_pliku(string_dzialanie):
    try:
        with open("kalkulator_dzialania.txt", "a") as plik:
            plik.write(string_dzialanie + "\n")
    except FileNotFoundError as e:
        print(f"Błąd: Nie odnaleziono pliku -> {e}")


def podaj_a():
    while True:
        var_a = input("\n\tPodaj wartość dla liczby 'a': ").replace(',', '.')
        try:
            var_a = float(var_a)
            break
        except ValueError:
            print("\tWartość 'a' musi być liczbą rzeczywistą")
    return var_a


def podaj_b():
    while True:
        var_b = input("\n\tPodaj wartość dla liczby 'b': ").replace(',', '.')
        try:
            var_b = float(var_b)
            break
        except ValueError:
            print("\tWartość 'b' musi być liczbą rzeczywistą")
    return var_b


def dodawanie(x, y):
    return x + y


def odejmowanie(x, y):
    return x - y


def mnozenie(x, y):
    return x * y


def dzielenie(x, y):
    return x / y


def pole_kola(x):
    return math.pi * x ** 2


def obwod_kola(x):
    return 2 * math.pi * x


while True:
    print("=======   MENU   =======")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("5. Pole koła")
    print("6. Obwód koła")
    print("7. Wyjście")
    opcja = input("Wybierz opcje: ")
    opcja_string = str(opcja)
    a = 0
    b = 0

    if opcja_string == "1" or opcja_string == "2" or opcja_string == "3":
        a = podaj_a()
        b = podaj_b()
    if opcja_string == "4":
        a = podaj_a()
        b = podaj_b()
        while b == 0:
            print("\tWartość 'b' nie może wynosić 0")
            b = podaj_b()
    if opcja_string == "5" or opcja_string == "6":
        a = podaj_a()
        while a <= 0:
            print("\tWartość 'a' musi być większa od 0")
            a = podaj_a()

    dzialanie = ""
    if opcja_string == "1":
        dzialanie = "{0} + {1} = {2}".format(str(a), str(b), str(dodawanie(a, b)))
    elif opcja_string == "2":
        dzialanie = "{0} - {1} = {2}".format(str(a), str(b), str(odejmowanie(a, b)))
    elif opcja_string == "3":
        dzialanie = "{0} * {1} = {2}".format(str(a), str(b), str(mnozenie(a, b)))
    elif opcja_string == "4":
        dzialanie = "{0} / {1} = {2}".format(str(a), str(b), str(dzielenie(a, b)))
    elif opcja_string == "5":
        dzialanie = "Pole koła o promieniu {0} wynosi {1}".format(str(a), str(round(pole_kola(a), 2)))
    elif opcja_string == "6":
        dzialanie = "Obwód koła o promieniu {0} wynosi {1}".format(str(a), str(round(obwod_kola(a), 2)))
    elif opcja_string == "7":
        print("\nKoniec programu!")
        break
    else:
        print("\nNie ma takiej opcji do wyboru, spróbuj ponownie")

    if opcja_string in map(str, range(1, 7)):
        print(f"\n\t\t{dzialanie}")
        zapis_do_pliku(dzialanie)
    print("\n\n")
