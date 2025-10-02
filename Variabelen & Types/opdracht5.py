# Opdracht:

# Vraag de gebruiker om twee getallen via input().

# Zet beide om naar int.

# Maak variabelen voor:

# de som

# het verschil (eerste - tweede)

# het product (keer)

# het quotiënt (delen, let op: eerste / tweede)
nummers = []
for i in range(1, 3):
    user_input = int(input(f"Voer een getal nummer {i} in "))
    if i == 2:
     while user_input == 0:
        print("Sorry getal 0 mag niet ingevoerd worden, probeer nog eens")
        user_input = int(input(f"Voer een getal nummer {i} in "))
    nummers.append(user_input)
     
som = sum(nummers)
verschil = nummers[0] - nummers[1]
product = nummers[0] * nummers[1]
quotiënt = nummers[0] / nummers[1]

print(f"De som van {nummers[0]} en {nummers[1]} is {som}")
print(f"Het verschil van {nummers[0]} en {nummers[1]} is {verschil}")
print(f"Het product van {nummers[0]} en {nummers[1]} is {product}")
print(f"Het quotiënt van {nummers[0]} en {nummers[1]} is {quotiënt:.3f}")