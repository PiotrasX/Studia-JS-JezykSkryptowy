import random


def lotto():
    tab = []
    while len(tab) < 6:
        czy_mozna = True
        liczba = random.randint(1, 49)
        for liczba_tab in tab:
            if liczba_tab == liczba:
                czy_mozna = False
                break
        if czy_mozna:
            tab.append(liczba)
    return tab


liczby = lotto()
print("Wylosowane liczby:", liczby)
