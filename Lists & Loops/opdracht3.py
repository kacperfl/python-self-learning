# Opdracht 3

# Schrijf een functie die een lijst van getallen binnenkrijgt en het volgende doet:

# Verwijder alle negatieve getallen uit de lijst.

# Kwadrateer vervolgens elk positief getal in de lijst.

# Return de nieuwe lijst én het gemiddelde van die kwadraten.

def uitwerker(lijst):
    positief_lijst = []
    for cijfer in lijst:
        if cijfer > 0:
            kwadraat_getal = cijfer ** 2
            positief_lijst.append(kwadraat_getal)
    gemiddlede = sum(positief_lijst) / len(positief_lijst)
    return positief_lijst, gemiddlede

lst = [-1, -3, 12, -5, 6, 23, 6, -1, -1]
print(f"De content van de positief en gekwadraateerd lijst is:{uitwerker(lst)[0]}  \n En de gemiddeld er van is: {uitwerker(lst)[1]}")