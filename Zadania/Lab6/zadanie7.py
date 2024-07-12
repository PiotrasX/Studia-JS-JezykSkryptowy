import matplotlib.pyplot as plt

# Dane -> (wzrost, masa ciała)
dane = [(160, 65), (164, 68), (168, 71), (172, 74), (176, 77), (180, 81), (184, 85), (188, 89), (192, 94), (196, 99),
        (200, 105)]

wzrost = [d[0] for d in dane]
masa_ciala = [d[1] for d in dane]

plt.scatter(wzrost, masa_ciala, color='red', marker='o')
plt.title('Zależność masy ciała od wzrostu')
plt.xlabel('Wzrost (cm)')
plt.ylabel('Masa ciała (kg)')
plt.grid(True)
plt.show()
