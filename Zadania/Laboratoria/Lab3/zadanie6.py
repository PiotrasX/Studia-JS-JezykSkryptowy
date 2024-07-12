import random

ranga = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'D', 'K', 'A']
kolor = ['c', 'd', 'h', 's']


def deck_new():
    lista = []
    for x_ranga in ranga:
        for x_kolor in kolor:
            krotka = (x_ranga, x_kolor)
            lista.append(krotka)
    return lista


def shuffle_deck(deck):
    random.shuffle(deck)
    return deck


def deal(deck, n: int):
    if 0 < n <= 10:
        talia_graczy = []
        for player in range(n):
            talia_gracza = [deck.pop() for _ in range(5)]
            talia_graczy.append(talia_gracza)
        return talia_graczy
    else:
        print("Liczba graczy musi wynosić od 1 do 10!")
        return None


lista_kart = deck_new()
lista_kart = shuffle_deck(lista_kart)
talia = deal(lista_kart, 3)
if talia is not None:
    gracz = 1
    for wiersz in talia:
        print(f"Gracz {gracz}:", wiersz)
        gracz += 1
