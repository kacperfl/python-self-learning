# Schrijf een programma waarin de computer een geheim getal kiest (bijv. tussen 1 en 10).
# De gebruiker moet blijven raden tot hij het juiste getal invoert.
# Gebruik een while-loop om te blijven herhalen.

# Eisen:

# Gebruik random.randint(1, 10) voor het geheime getal.

# Vraag in een loop om invoer.

# Zeg bij elke poging of het getal te hoog of te laag is.

# Stop de loop als het getal goed is, en print het aantal pogingen.

import random

getal = random.randint(1, 40)
pogingen = 0

while True:
    user_input = int(input("Gok het getal: "))
    pogingen += 1

    if user_input == getal:
        print(f"Goed zo! Je hebt het geraden in {pogingen} pogingen.")
        break
    elif user_input > getal:
        print("Te hoog!")
    elif pogingen == 5:
        print(f"U heeft 5 {pogingen} gedaan, de game stopt")
        break
    else:
        print("Te laag!")

       