# Maak een lijst van minimaal 8–10 getallen, met positieve en negatieve waarden.

# Gebruik een while-loop om één voor één door de lijst te gaan.

# Binnen de loop controleer je elk getal:

# Als het getal positief is, verdubbel het en voeg het toe aan een nieuwe lijst.

# Als het getal negatief is, negeer het of sla het over.

# Houd een teller bij van hoeveel getallen zijn verwerkt.

# Stop de loop zodra alle getallen uit de lijst zijn bekeken.

# Bereken en toon uiteindelijk:

# De nieuwe lijst met alleen de verwerkte positieve getallen

# Het totaal van de nieuwe lijst

# Het gemiddelde van de nieuwe lijst
teller = 0
getallen_lijst = [5, -12, 0, 45, -3, 100, -78, 1, -9, 22]
new_lst = []
index = 0


while index < len(getallen_lijst):
    huidig_getal = getallen_lijst[index]
    if huidig_getal < 0:
        index += 1
        continue
    else:
        huidig_getal > 0
        teller += 1
        index += 1
        verdubellen = huidig_getal * 2
        new_lst.append(verdubellen)

    
gemiddelde = sum(new_lst) / len(new_lst)
print(f"De som is: {sum(new_lst)}, de gemiddelde is: {gemiddelde}, en de aantal positieve getallen zijn: {teller}")
