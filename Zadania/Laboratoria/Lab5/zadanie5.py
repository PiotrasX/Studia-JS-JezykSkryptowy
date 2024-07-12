class Liczba:
    def __init__(self, liczba):
        self.liczba = liczba

    def __xor__(self, druga_liczba):
        return self.liczba * self.liczba + 2 * self.liczba * druga_liczba.liczba + druga_liczba.liczba


x = Liczba(5)
y = Liczba(7)
wynik = x ^ y
print(wynik)
