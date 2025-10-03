# Maak een functie die één getal als input krijgt.

# Laat de functie het kwadraat van dat getal berekenen.

# Roep de functie aan met een testgetal (bijv. 4) en print het resultaat.


def kwadraat(invoer):
    return invoer ** 2

user = int(input("Voer een getal in: "))

print(f"De kwadraat getal is: {kwadraat(user)}")