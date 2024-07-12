def sumowanie(lista):
    suma_elementow = 0
    for liczba_lista in lista:
        suma_elementow += liczba_lista
    return suma_elementow


def odczyt(suma_funkcja):
    try:
        with open("liczby.txt") as plik:
            for linia in plik:
                tekst = linia.strip().replace(",", ".")
                try:
                    liczba = float(tekst)
                    lista_liczb.append(liczba)
                except ValueError:
                    continue
        return suma_funkcja(lista_liczb)
    except FileNotFoundError as e:
        print(f"Błąd: Nie odnaleziono pliku -> {e}")


lista_liczb = []
suma = odczyt(sumowanie)
print("Lista z liczbami odczytanymi z pliku:", lista_liczb)
print("Suma elementów na liście:", suma)
