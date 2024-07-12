def dodawaj_tekst(tekst):
    i = tekst
    j = 1
    while j <= len(i):
        yield i[0:j]
        j += 1


lista = list(dodawaj_tekst("spam"))
print(lista)
