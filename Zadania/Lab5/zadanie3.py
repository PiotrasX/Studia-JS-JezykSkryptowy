class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def wypisz_info(self):
        print(f"[Osoba] Imie: {self.imie}, Nazwisko: {self.nazwisko}")


class Student(Osoba):
    def __init__(self, imie, nazwisko, numer_albumu):
        super().__init__(imie, nazwisko)
        self.numer_albumu = numer_albumu

    def wypisz_info(self):
        print(f"[Student] Imie: {self.imie}, Nazwisko: {self.nazwisko}, Numer albumu: {self.numer_albumu}")


osoba1 = Osoba("Janusz", "Kowalski")
osoba2 = Osoba("Małgorzata", "Nowacka")
osoba3 = Osoba("Michalina", "Ździebło")
lista_osob = [osoba1, osoba2, osoba3]
for x in lista_osob:
    x.wypisz_info()

print()

student1 = Student("Maks", "Przypiek", 125155)
student2 = Student("Łukasz", "Powrotny", 125157)
student3 = Student("Piotr", "Rojek", 125159)
lista_studentow = [student1, student2, student3]
for x in lista_studentow:
    x.wypisz_info()
