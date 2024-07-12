import matplotlib.pyplot as plt
import numpy as np
import requests

# Podaj swój klucz API OpenWeatherMap
api_key = "7a44285f2b6c4bee04cb011236bcb5a0"

# Utwórz listę współrzędnych geograficznych miast w Europie
coordinates = [
    (51.509865, -0.118092),     # Londyn
    (48.856613, 2.352222),      # Paryż
    (52.520008, 13.404954),     # Berlin
    (40.416775, -3.703790),     # Madryt
    (41.902782, 12.496366),     # Rzym
    (52.229676, 21.012229)      # Warszawa
]

towns = ['Londyn', 'Paryż', 'Berlin', 'Madryt', 'Rzym', 'Warszawa']

# Pobierz dane temperatury dla każdego z miast
temperatures = []
for latitude, longitude in coordinates:
    response = requests.get("http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&units=metric&appid={}"
                            .format(latitude, longitude, api_key))
    data = response.json()
    if 'main' in data:
        temperature = data['main']['temp']
        temperatures.append(temperature)
    else:
        print(f"Nie udało się pobrać danych dla współrzędnych: ({latitude}, {longitude})")


# Sprawdź, czy wszystkie dane zostały pobrane
if len(temperatures) != len(coordinates):
    print("Nie udało się pobrać wszystkich danych temperatur")
else:
    # Stwórz tablicę numpy z danymi temperatury
    temperatures = np.array(temperatures).reshape(1, -1)

    # Stwórz mapę cieplną z danymi temperatury
    plt.imshow(temperatures, cmap='coolwarm', aspect='auto')
    plt.colorbar(label='Temperatura w °C')

    # Definicja podpisów osi
    ax = plt.gca()
    ax.set_yticks([])
    ax.set_xticks(np.arange(len(towns)))
    ax.set_xticklabels(towns)

    # Dodanie wartości temperatury na mapie cieplnej
    for i in range(len(towns)):
        plt.text(i, 0, f'{temperatures[0, i]:.1f}°C', ha='center', va='center', color='black')

    # Pokaż wykres
    plt.title('Temperatury w miastach Europy')
    plt.show()
