# Wat je moet doen:

# Maak een functie die twee getallen als parameters krijgt.

# Laat de functie de som van de twee getallen berekenen en teruggeven.

# Roep de functie meerdere keren aan met verschillende testgetallen en print de resultaten.


def uitrekening(x,y):
    return x + y

user = int(input("Voer een getal in: "))
user2 = int(input("Voer een getal in: "))

print(f"De som van {user} en de {user2} is {uitrekening(user,user2)}")