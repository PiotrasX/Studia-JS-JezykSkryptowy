import random
from array import array

tablica = array("d")
for x in range(10):
    cyfra = round(random.uniform(-5, 5), 3)
    tablica.append(cyfra)

try:
    with open("result.txt", "w") as plik:
        for x in tablica:
            plik.write(f"{x:0.3f}\n")
except FileNotFoundError as e:
    print(f"Błąd: Nie odnaleziono pliku -> {e}")
