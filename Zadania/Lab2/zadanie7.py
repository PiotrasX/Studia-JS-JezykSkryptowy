import math


def rownanie_kwadratowe(a, b, c):
    delta = b * b - 4 * a * c

    if a == 0:
        dzialanie = f"a = {a}\t\tb = {b}\t\tc = {c}\nTo nie jest równanie kwadratowe, ponieważ a = 0."
    elif delta < 0:
        dzialanie = f"a = {a}\t\tb = {b}\t\tc = {c}\nDelta mniejsza od 0.\n"\
                    f"Brak rozwiązania w zbiorze liczb rzeczywistych."
    elif delta == 0:
        x = (-b) / 2 * a
        dzialanie = f"a = {a}\t\tb = {b}\t\tc = {c}\nDelta równa 0.\n"\
                    f"Jedno rozwiązanie w zbiorze liczb rzeczywistych.\nx = {x}"
    else:
        x1 = (-b - math.sqrt(delta)) / 2 * a
        x2 = (-b + math.sqrt(delta)) / 2 * a
        dzialanie = (f"a = {a}\t\tb = {b}\t\tc = {c}\nDelta większa od 0.\n"
                     f"Dwa rozwiązania w zbiorze liczb rzeczywistych.\nx1 = {x1}\nx2 = {x2}")

    try:
        with open("result.txt", "a") as plik:
            plik.write(dzialanie + "\n\n")
    except FileNotFoundError as e:
        print(f"Błąd: Nie odnaleziono pliku -> {e}")
    print("\n", dzialanie)


def podaj_liczbe(tekst):
    while True:
        try:
            liczba_string = input(tekst).replace(",", ".")
            liczba = float(liczba_string)
            return liczba
        except ValueError:
            print("Musisz podać wartość typu 'float'!")


aa = podaj_liczbe("\nPodaj parametr 'a': ")
bb = podaj_liczbe("\nPodaj parametr 'b': ")
cc = podaj_liczbe("\nPodaj parametr 'c': ")
rownanie_kwadratowe(aa, bb, cc)
