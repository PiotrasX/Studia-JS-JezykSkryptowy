import numpy as np


def tworz_tab():
    tab = np.zeros((5, 5), dtype=np.uint64)
    tab[0] = [2, 3, 4, 5, 6]
    for wiersz in range(1, len(tab)):
        for kolumna in range(0, len(tab[wiersz])):
            tab[wiersz][kolumna] = pow(tab[wiersz - 1][kolumna], 2)
    return tab


tablica = tworz_tab()
print(tablica)
