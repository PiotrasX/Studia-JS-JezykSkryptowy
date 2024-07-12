from datetime import date

dzisiejsza_data = date.today()
print("Data systemowa: " + str(dzisiejsza_data))

rok = int(input("Podaj rok: "))
miesiac = int(input("Podaj miesiąc: "))
dzien = int(input("Podaj dzień: "))
twoja_data = date(rok, miesiac, dzien)

liczba_dni = dzisiejsza_data - twoja_data
print("Liczba dni od twojej daty do aktualnej daty:", liczba_dni.days)
