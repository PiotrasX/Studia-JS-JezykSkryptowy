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


while True:
    print("=======   MENU   =======")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("5. Wyjście")
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

    if opcja_string == "1":
        print("\n\t\t" + str(a) + " + " + str(b) + " = " + str(a + b))
    elif opcja_string == "2":
        print("\n\t\t" + str(a) + " - " + str(b) + " = " + str(a - b))
    elif opcja_string == "3":
        print("\n\t\t" + str(a) + " * " + str(b) + " = " + str(a * b))
    elif opcja_string == "4":
        print("\n\t\t" + str(a) + " / " + str(b) + " = " + str(a / b))
    elif opcja_string == "5":
        print("\nKoniec programu!")
        break
    else:
        print("\nNie ma takiej opcji do wyboru, spróbuj ponownie")
    print("\n\n")
