# Opdracht 4

# Schrijf een functie die een lijst van getallen ontvangt en het volgende doet:

# Verwijder alle negatieve getallen.

# Maak een nieuwe lijst met alle getallen groter dan een door de gebruiker ingevoerd getal.

# Bereken het gemiddelde van deze nieuwe gefilterde lijst.

# Return de gefilterde lijst én het gemiddelde.

def uitwerker(lijst):
    positief_lijst = []
    bigger_then_users = []
    
    for num in lijst:
        if num > 0:
            positief_lijst.append(num)
            
    for getal in positief_lijst:
        if user_input < getal:
            bigger_then_users.append(getal)
    gemiddelde = sum(bigger_then_users) / len(bigger_then_users)
    return bigger_then_users, gemiddelde
            
user_input = int(input("Voer een getal in: "))  
lst = [-1, -3, 12, -5, 6, 23, 6, -1, 1]
print(f"De lijst van getalen grooter dan ingevulde door jou is: {uitwerker(lst)[0]} en de gemiddelde daarvan is: {uitwerker(lst)[1]}")