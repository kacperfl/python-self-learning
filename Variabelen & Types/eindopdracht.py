# Opdracht:
# Maak een mini-rekenmachine met deze regels:

# Vraag de gebruiker om twee getallen.

# Vraag de gebruiker om een bewerking: "+", "-", "*", of "/".

# Gebruik variabelen om de juiste berekening uit te voeren.

# Print het resultaat in een duidelijke zin, bijvoorbeeld:

# 8 * 3 = 24


# Extra uitdaging: als de gebruiker een ongeldige bewerking invoert (bijvoorbeeld % of tekst), print dan:
# "Ongeldige bewerking."

# Extra extra uitdaging: zorg dat delen door nul niet crasht, maar in plaats daarvan "Delen door nul is niet toegestaan." print.
nummers = []
for i in range(1, 3):
    user = (input(f"Voer een getal {i} uit: "))
    while True:
        if user == "":
            print("U heeft geen waarde ingevoerd, probeer nog eens")
            user = (input(f"Voer een getal {i} uit: "))
        elif user.isdigit() == False:
            print("De invoer is geen cijfer!")
            user = (input(f"Voer een getal {i} uit: "))
        else:
            break
    int_num = int(user)
    nummers.append(int_num)

teken = input("Voer een teken uit: ")
while True:
    if teken != "+" and teken != "-" and teken != "*" and teken != "/":
        print("U heeft geen speciaal teken gebruikt, probeer het nog eens")
        teken = input("Voer een teken uit: ")
    else:
        break
resultaat = ""
if teken == "+":
    resultaat = nummers[0] + nummers[1]
elif teken == "-":
    resultaat = nummers[0] - nummers[1]
elif teken == "*":
    resultaat = nummers[0] * nummers[1]
elif teken == "/":
    resultaat = nummers[0] / nummers[1]

print(f"De uitwerking is: {nummers[0]} {teken} {nummers[1]} = {resultaat:.2f}")
