def histogram(lokalizacja):
    slownik = {}
    try:
        with open(lokalizacja, "r") as plik:
            tekst = plik.read()
            tekst = tekst.replace(" ", "")
            tekst = tekst.replace("\n", "")
            tekst = tekst.replace("\t", "")
            tekst_bez_bialych_znakow = tekst
        for litera in tekst_bez_bialych_znakow:
            if slownik.get(litera) is None:
                slownik[litera] = 1
            else:
                slownik[litera] += 1
        return slownik
    except FileNotFoundError as e:
        print(f"Błąd: Nie odnaleziono pliku -> {e}")
        return None


histogram = histogram("document.txt")
print(histogram)
