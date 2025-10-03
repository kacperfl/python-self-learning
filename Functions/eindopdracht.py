# Wat je moet doen:

# Maak een functie die een lijst van getallen als parameter krijgt.

# Binnen de functie:

# Vraag de gebruiker een keuze:

# "max" → geef het grootste getal terug

# "min" → geef het kleinste getal terug

# "avg" → geef het gemiddelde terug

# "kwadraat" → geef een nieuwe lijst met de kwadraten van alle positieve getallen

# "filter" → vraag een getal n en geef een lijst terug met alleen de getallen groter dan n

# Controleer of de keuze geldig is; zo niet, vraag opnieuw.

# Roep de functie aan met een testlijst van minstens 10 getallen, inclusief negatieve getallen.

# Print het resultaat netjes afhankelijk van de keuze.


def function(lijst):
    kwadrtaat_lst = []
    positief_lst = []
    filter_lst = []
    userInput = input("Voer een opdracht uit: (max, min, avg, kwadrtaat, filter)")
    
    while True:
        if userInput != "max" and userInput != "min" and userInput != "avg" and userInput != "kwadraat" and userInput != "filter":
            print(f"U heeft een verkeerd waarde getoets, probeer nog eens")
            userInput = input("Voer een nieuwe opdracht uit: (max, min, avg, kwadrtaat, filter)")
        else:
            break
    while True:
        
        if userInput == "max":
            return max(lijst)
        elif userInput == "min":
            return min(lijst)
        elif userInput == "avg":
            return sum(lijst) / len(lijst)
        elif userInput == "kwadraat":
            for cijfer in lijst:
                if cijfer > 0:
                    positief_lst.append(cijfer)
            for pos_cijfer in positief_lst:
                kwadraat = pos_cijfer ** 2
                kwadrtaat_lst.append(kwadraat)
            return kwadrtaat_lst
        elif userInput == "filter":
            filter_input = int(input("Voer een getal uit, en krijg resultaten hoger dan dat getal:"))
            for num in lijst:
                if filter_input < num:
                    filter_lst.append(num)
            return f"Alle getalen grooter dan {filter_input} zijn: {filter_lst}"

lst = [2, 5, 8, 23, 76, 23, -3, -2, 2, -65, -12, 3]
resultaat = function(lst)
print(resultaat)
