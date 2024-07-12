import matplotlib.pyplot as plt

data = [('jabłka', 30), ('gruszki', 20), ('śliwki', 15), ('banany', 25), ('cytryny', 10)]
etykiety = []
rozmiary = []

for i in data:
    etykiety.append(i[0])
    rozmiary.append(i[1])

fig, ax = plt.subplots()
ax.pie(rozmiary, labels=etykiety, autopct='%1.1f%%', shadow=True, startangle=90)
ax.axis('equal')
plt.title('Procentowy udział różnych owoców w koszu')
plt.show()
