# Wat je moet doen:

# Maak een functie die een lijst van getallen als parameter krijgt.

# Laat de functie:

# Het maximum en minimum van de lijst vinden.

# De som van alle getallen berekenen.

# Laat de functie alle drie de resultaten teruggeven (max, min, som).

# Roep de functie aan met een lijst van 5 testgetallen die je zelf kiest, en print alle resultaten netjes.


def uitwerking(lijst):
    return max(lijst), min(lijst), sum(lijst)

lst = [12, 23, 54, 5, 8, -4, 74]
resultaat = uitwerking(lst)
print(f"De maximum getal van lijst is: {resultaat[0]} en de minimum is {resultaat[1]}, en de geheel som is: {resultaat[2]}")
