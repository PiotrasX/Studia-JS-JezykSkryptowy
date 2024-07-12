import random

""" Programowanie obiektowe — klasy """

# Klasy są tworzone przy użyciu słowa kluczowego class i wciętych bloków, które zawierają metody klas
# (które są funkcjami). Poniżej znajduje się przykład prostej klasy i jej obiektów.


class Cat:
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs
# Ten kod definiuje klasę o nazwie Cat, która ma dwa atrybuty: color i legs. Następnie klasa służy do tworzenia
# trzech oddzielnych obiektów (reprezentantów) tej klasy.


felix = Cat("ginger", 4)
rover = Cat("dog-colored", 4)
stumpy = Cat("brown", 3)

print("felix.color ->", felix.color)
print("felix.legs ->", felix.legs)
print()

# Metoda __init__ jest najważniejszą metodą w klasie. Jest ona wywoływana, gdy tworzona jest instancja (obiekt) klasy,
# używając nazwy klasy jako funkcji.

# Wszystkie metody muszą mieć self jako pierwszy parametr, chociaż nie jest on jawnie przekazywany, Python dodaje
# za ciebie argument self — nie trzeba go uwzględniać, gdy wywołuje się metodę. W definicji metody self odnosi się do
# instancji wywołującej metodę.

# Instancje klasy mają atrybuty, które są związanymi z nimi fragmentami danych. W tym przykładzie instancje klasy Cat
# mają atrybuty color i legs. Dostęp do nich można uzyskać, umieszczając kropkę i nazwę atrybutu po instancji.
# W metodzie __init__ można użyć self.atrybut do ustawienia początkowej wartości atrybutów instancji.

# W powyższym przykładzie metoda __init__ pobiera dwa argumenty i przypisuje je do atrybutów obiektu. Metoda __init__
# jest konstruktorem klasy.



""" Programowanie obiektowe — metody """

# Klasy mogą mieć zdefiniowane inne metody w celu dodania do nich funkcjonalności. Należy pamiętać, że wszystkie
# metody muszą mieć self jako pierwszy parametr. Dostęp do tych metod można uzyskać za pomocą taki sam sposób jak
# do atrybutów, czyli przy pomocy składni z kropką.


class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    @staticmethod
    def bark():
        print("Woof!")


fido = Dog("Fido", "brown")
print("fido.name ->", fido.name)
fido.bark()
print()

# Klasy mogą również posiadać atrybuty klas, utworzone przez przypisanie zmiennych w treści klasy. Dostęp do nich
# można uzyskać z instancji klasy lub samej klasy.


class Dog:
    legs = 4

    def __init__(self, name, color):
        self.name = name
        self.color = color


fido = Dog("Fido", "brown")
print("fido.name ->", fido.name)
print("fido.legs ->", fido.legs)
print("Dog.legs ->", Dog.legs)
print()
# Atrybuty klas są wspólne dla wszystkich instancji klasy.



""" Programowanie obiektowe — dziedziczenie """

# Dziedziczenie zapewnia sposób udostępniania funkcji między klasami. Wyobraź sobie kilka klas, Cat, Dog, Rabbit,
# i tak dalej. Chociaż mogą się różnić pod pewnymi względami (tylko pies może mieć jakąś metodę), prawdopodobnie będą
# podobne w innych (wszystkie mają atrybuty kolor i imię). Podobieństwo to można wyrazić, czyniąc je wszystkie
# dziedziczącymi z superklasy Animal, która zawiera wspólną funkcjonalność. Aby dziedziczyć klasę z innej klasy,
# umieść nazwę nadklasy w nawiasach po nazwie klasy.


class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color


class Cat(Animal):
    @staticmethod
    def purr():
        print("Purr...")


class Dog(Animal):
    @staticmethod
    def bark():
        print("Woof!")


print("------------------------------")
fido = Dog("Fido", "brown")
print("nazwa klasy ->", fido.__class__.__name__)
print("fido.color ->", fido.color)
fido.bark()
print()

maucaty = Cat("Maucaty", "grey")
print("nazwa klasy ->", maucaty.__class__.__name__)
print("maucaty.color ->", maucaty.color)
maucaty.purr()
print("------------------------------")
print()

# Klasa, dziedzicząca z innej klasy nazywana jest podklasą. Klasa, po której dziedziczą inne klasy, nazywana jest
# superklasą. Jeśli klasa dziedziczy po innej z tymi samymi atrybutami lub metodami, nadpisuje je.


class Wolf:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("Grr...")


class Dog(Wolf):
    def bark(self):
        print("Woof!")


print("------------------------------")
rufus = Wolf("Rufus", "white")
print("nazwa klasy ->", rufus.__class__.__name__)
print("rufus.color ->", rufus.color)
rufus.bark()
print()

maxus = Dog("Maxus", "grey")
print("nazwa klasy ->", maxus.__class__.__name__)
print("maxus.color ->", maxus.color)
maxus.bark()
print("------------------------------")
print()
# W powyższym przykładzie Wolf jest superklasą, Dog jest podklasą.

# Dziedziczenie może być również pośrednie. Jedna klasa może dziedziczyć od innej i ta klasa może dziedziczyć
# z trzeciej klasy.


class A:
    @staticmethod
    def method():
        print("A method")


class B(A):
    @staticmethod
    def another_method():
        print("B method")


class C(B):
    @staticmethod
    def third_method():
        print("C method")


c = C()
c.method()
c.another_method()
c.third_method()
print()

# Funkcja super jest użyteczną funkcją związaną z dziedziczeniem, która odnosi się do klasy nadrzędnej.
# Można jej użyć do znalezienia metody o określonej nazwie w nadklasie obiektu.


class A:
    def spam(self):
        print(1)


class B(A):
    def spam(self):
        print(2)
        super().spam()
        # super().spam() -> wywołuje metodę spam z nadklasy


B().spam()
print()



""" Programowanie obiektowe — magiczne metody """

# Magiczne metody są specjalnymi metodami, które mają podwójne podkreślenia na początku i na końcu ich nazw.
# Jak dotąd jedynym, z którym się spotkaliśmy, jest __init__, ale jest jeszcze kilka innych. Są używane do tworzenia
# funkcjonalności, które nie mogą być reprezentowane jako normalna metoda.

# Jednym z ich powszechnych zastosowań jest przeciążanie operatorów. Oznacza to zdefiniowanie operatorów dla
# niestandardowych klas, które pozwalają na użycie operatorów takich jak '+' i '*'. Przykładową magiczną metodą jest
# __add__ dla '+'.


class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def to_str(self):
        return self.x, self.y


first = Vector2D(5, 7)
second = Vector2D(3, 9)
result = first + second
print("'first' vector ->", first.to_str())
print("'second' vector ->", second.to_str())
print("'result' vector ->", result.to_str())
print()
# Metoda __add__ pozwala na zdefiniowanie niestandardowego zachowania operatora '+' w klasie. Jak widać, dodaje
# odpowiednie atrybuty obiektów i zwraca nowy obiekt, zawierający wynik. Po zdefiniowaniu można razem dodać dwa obiekty
# danej klasy. Jeśli nie byłaby zdefiniowana, takie dodawanie byłoby niemożliwe.
# Wyrażenie x + y jest tłumaczone na x.__add__(y).

#   Metoda	      |   Operator
#   --------------------------
#   __add__       |   +
#   __sub__	      |   -
#   __mul__	      |   *
#   __truediv__	  |   /
#   __floordiv__  |   //
#   __mod__	      |   %
#   __pow__	      |   **
#   __and__	      |   &
#   __xor__	      |   ^
#   __or__	      |   |


class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __truediv__(self, other):
        line = "=" * len(other.cont)
        return "\n".join([self.cont, line, other.cont])


spam = SpecialString("spam")
hello = SpecialString("Hello world!")
print(spam / hello)
print()

# Python dostarcza również magiczne metody do porównań.

#   Metoda	      |   Operator
#   --------------------------
#   __lt__	      |   <
#   __le__	      |   <=
#   __eq__	      |   ==
#   __ne__	      |   !=
#   __gt__	      |   >
#   __ge__	      |   >=


class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __gt__(self, other):
        text = ""
        for index in range(len(other.cont) + 1):
            component = other.cont[:index] + ">" + self.cont
            component += ">" + other.cont[index:]
            text += component + "\n"
        return text


spam = SpecialString("spam")
eggs = SpecialString("eggs")
result = spam > eggs
print(result)
# Jak widać, można zdefiniować dowolne niestandardowe zachowanie dla przeciążonych operatorów.

# Istnieje kilka magicznych metod tworzenia klas, które działają jak kontenery.
# * __len__ dla len(),
# * __getitem__ dla indeksowania,
# * __setitem__ dla przypisania do wartości indeksowanych,
# * __delitem__ do usuwania indeksowanych wartości,
# * __iter__ dla iteracji obiektów (np.: dla pętli),
# * __contains__ dla sprawdzenia zawierania,

# Istnieje wiele innych metod magicznych, takich jak __call__ dla wywoływania obiektów jako funkcji i __int__, __str__,
# i tym podobne, do konwersji obiektów na typy wbudowane.


class VagueList:
    def __init__(self, cont):
        self.cont = cont

    def __getitem__(self, index):
        return self.cont[index + random.randint(-1, 1)]

    def __len__(self):
        return random.randint(0, len(self.cont) * 2)


vague_list = VagueList(["A", "B", "C", "D", "E"])
print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[2])
print()
# Funkcja len() klasy VagueList została przesłonięta, aby zwrócić losową liczbę. Funkcja indeksowania zwraca również
# losowy element z zakresu listy na podstawie wyrażenia.



""" Cykl życia obiektów """

# Cykl życia obiektu składa się z jego tworzenia, manipulacji i destrukcji.

# Pierwszym etapem cyklu życia obiektu jest definicja klasy, do której należy. Następnym etapem jest tworzenie
# instancji danego typu, gdy wywoływana jest funkcja __init__. Pamięć jest przydzielona, aby przechowywać utworzoną
# instancję. Tuż przed tym zdarzeniem wywoływana jest metoda __new__ klasy. Jest ona przesłaniana tylko w specjalnych
# przypadkach. Po tym zdarzeniu obiekt jest gotowy do użycia.

# Inny kod może następnie wchodzić w interakcję z obiektem, wywołując na nim funkcje i uzyskując dostęp do jego
# atrybutów. W końcu zostanie wykorzystany i może zostać zniszczony.

# Gdy obiekt zostanie zniszczony, pamięć przydzielona do niego zostanie zwolniona i może być wykorzystana do innych
# celów. Zniszczenie obiektu następuje, gdy jego licznik odniesienia(referencji) osiągnie zero. Liczba referencyjna
# to liczba zmiennych i innych elementów odnoszących się do obiektu. Jeśli nic nie odnosi się do obiektu (ma zerową
# wartość odniesienia), nic nie może z nim współdziałać, więc można go bezpiecznie usunąć.

# W niektórych sytuacjach dwa (lub więcej) obiekty mogą być przywoływane tylko przez siebie, dlatego też można je
# usunąć. Instrukcja del zmniejsza liczbę odwołań obiektu o jeden, co często prowadzi do jego usunięcia. Magiczną
# metodą jest __del__. Liczba odwołań do obiektu wzrasta, gdy jest przypisana nowa nazwa lub umieszczona w kontenerze
# (liście, krotce lub słowniku). Liczba odwołań obiektu zmniejsza się, gdy zostanie usunięta za pomocą metody __del__,
# odniesienie zostanie ponownie przypisane lub jego odwołanie wykracza poza zakres. Kiedy licznik odwołań do obiektu
# osiąga zero, Python automatycznie go usuwa.



""" Ukrywanie danych - enkapsulacja """

# Ukrywanie danych to stwierdzenie, że szczegóły implementacji klasy powinny być ukryte, a dla tych, którzy chcą
# korzystać z klasy, prezentowany jest czysty, standardowy interfejs. W innych językach programowania zwykle odbywa
# się to za pomocą prywatnych metod i atrybutów, które blokują zewnętrzny dostęp do określonych metod i atrybutów
# w klasie. Filozofia Pythona jest nieco inna. Często jest to określone jako "wszyscy tutaj jesteśmy dorośli",
# co oznacza, że nie powinno się nakładać arbitralnie ograniczeń dostępu do części klasy. Dlatego nie ma sposobów
# na wymuszenie, aby metoda lub atrybut, był ściśle prywatny.

# Istnieją jednak sposoby zniechęcenia ludzi do uzyskiwania dostępu do części klasy, na przykład poprzez oznaczenie,
# że jest to szczegół implementacji i będą one używane na własne ryzyko.

# Słabo prywatne metody i atrybuty mają na początku jedno podkreślenie. Oznacza to, że są one prywatne i nie powinny
# być używane przez zewnętrzny kod. Jednak jest to głównie konwencja i nie blokuje dostępu do kodu zewnętrznego.

# Silnie prywatne metody i atrybuty mają podwójne podkreślenie na początku ich nazw. To powoduje, że ich nazwy są
# zniekształcone, co oznacza, że nie można uzyskać do nich dostępu spoza klasy. Celem tego nie jest zapewnienie,
# że są one prywatne, ale unikanie błędów, gdy istnieją podklasy, które mają metody lub atrybuty o tych samych nazwach.



""" Metody klas """


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    @classmethod
    def new_square(cls, side_length):
        return cls(side_length, side_length)


square = Rectangle.new_square(5)
print("area -> ", square.calculate_area())
# 'new_square' jest metodą klasy i jest wywoływany w klasie, a nie w instancji klasy.
# Zwraca nowy obiekt klasy Rectangle.



""" Metody statyczne """

# Metody statyczne są podobne do metod klasowych, z tym wyjątkiem, że nie otrzymują żadnych dodatkowych argumentów.
# Są one identyczne z normalnymi funkcjami należącymi do klasy. Są one oznaczone adnotacją staticmethod.


class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @staticmethod
    def validate_topping(topping):
        if topping == "pineapple":
            raise ValueError("No pineapples!")
        else:
            return True


ingredients = ["cheese", "onions", "spam"]
if all(Pizza.validate_topping(i) for i in ingredients):
    pizza = Pizza(ingredients)
print()



""" Właściwości """

# Właściwości zapewniają sposób dostosowywania dostępu do atrybutów instancji. Są one tworzone przez umieszczenie
# adnotacji property nad metodą, co oznacza, że gdy zostanie wywołany atrybut instancji o tej samej nazwie co metoda,
# metoda zostanie wywołana. Jednym z typowych zastosowań właściwości jest ustawienie atrybutu jako atrybutu "tylko do
# odczytu".


class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @property
    def pineapple_allowed(self):
        return False


new_pizza = Pizza(["cheese", "tomato"])
print(new_pizza.pineapple_allowed)
# pizza.pineapple_allowed = True — wyrzuci błąd
