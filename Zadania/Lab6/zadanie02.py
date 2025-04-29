import matplotlib.pyplot as plt

fig, ax = plt.subplots()
dni_tygodnia = ['poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota', 'niedziela']
temperatury = [9, 16, 23, 26, 31, 24, 19]
bar_etykiety = []
bar_kolory = []

for temp in temperatury:
    if temp < 10:
        if 'Niska' in bar_etykiety:
            bar_etykiety.append('_Niska')
        else:
            bar_etykiety.append('Niska')
        bar_kolory.append('tab:blue')
    elif temp < 20:
        if 'Umiarkowana' in bar_etykiety:
            bar_etykiety.append('_Umiarkowana')
        else:
            bar_etykiety.append('Umiarkowana')
        bar_kolory.append('tab:green')
    elif temp < 30:
        if 'Średnia' in bar_etykiety:
            bar_etykiety.append('_Średnia')
        else:
            bar_etykiety.append('Średnia')
        bar_kolory.append('tab:orange')
    else:
        if 'Wysoka' in bar_etykiety:
            bar_etykiety.append('_Wysoka')
        else:
            bar_etykiety.append('Wysoka')
        bar_kolory.append('tab:red')

ax.bar(dni_tygodnia, temperatury, label=bar_etykiety, color=bar_kolory, width=0.7)
ax.set_ylim(0, 50)
ax.set_ylabel('Stopnie Celsjusza')
ax.set_title('Temperatury w poszczególnych dniach tygodnia')
ax.legend(title='Wartość temperatury')
plt.show()
