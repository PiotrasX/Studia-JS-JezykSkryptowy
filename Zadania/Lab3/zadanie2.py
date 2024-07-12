from array import array

tablica = array("u")
while True:
    znak = input("Podaj znak ('ENTER' kończy działanie pętli): ")
    if znak == "":
        break
    tablica.append(znak[0:1])

print("\nWprowadzona tablica:")
print(' '.join(map(str, tablica)))

print("\nWprowadzona tablica w odwrotnej kolejności:")
tablica.reverse()
print(' '.join(map(str, tablica)))
