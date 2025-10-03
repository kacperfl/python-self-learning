# Wat je moet doen:

# Maak een functie die een lijst van getallen als parameter krijgt.

# Binnen de functie:

# Filter eerst alle negatieve getallen uit de lijst.

# Bereken vervolgens voor de overgebleven getallen:

# Het kwadraat van elk getal.

# Het gemiddelde van de nieuwe kwadratenlijst.

# De functie moet twee dingen teruggeven:

# De lijst van kwadraten

# Het gemiddelde van die lijst

# Roep de functie aan met een testlijst van minstens 8 getallen, inclusief enkele negatieve getallen, en print de resultaten netjes.

def calc(lijst):
    positief_lst = []
    kwadraat_lijst = []
    for i in lijst:
        if i > 0:
            positief_lst.append(i)
    
    for cijfer in positief_lst:
        kwadraat = cijfer ** 2
        kwadraat_lijst.append(kwadraat)
    gemiddelde = sum(kwadraat_lijst) / len(kwadraat_lijst)
    return kwadraat_lijst, gemiddelde
 
lst = [2,5,8,23,76,23,-3,-2,2,-65,-12]
resultaat = calc(lst)
print(f"De kwadraat lijst is: {resultaat[0]} en de gemiddelde daarvan is {resultaat[1]:.4f}")