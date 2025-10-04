# Bewerk dezelfde matrix als in de vorige opdracht, maar voeg nu 2 nieuwe berekeningen toe:

# Bereken de som van alle positieve getallen (zoals je al doet).

# Bereken het gemiddelde van álle waarden in de nieuwe matrix.

# Tel hoeveel even en oneven getallen er uiteindelijk in de nieuwe matrix zitten.

# De functie moet een dictionary (woordenboek) teruggeven, bijvoorbeeld:


def nested_lst(lijst):
    nieuwe_matrix = []
    teller_pos = 0
    teller_kwa = 0

    for rij in lijst:
        nieuwe_rij = []
        for num in rij:

            if num < 0:
                continue
            elif num % 2 == 0:
                teller_pos += 1
                verdubbelen = num * 2
                nieuwe_rij.append(verdubbelen)
            elif num % 2 > 0:
                teller_kwa += 1
                kwadraat = num ** 2
                nieuwe_rij.append(kwadraat)
        nieuwe_matrix.append(nieuwe_rij)

    som = 0
    aantal = 0
    for reeks in nieuwe_matrix:
        totaal = sum(reeks)
        som += totaal

        lengte = len(reeks)
        aantal += lengte
    gemiddelde = som / aantal
    
    thisdict = {"Nieuwe matrix": nieuwe_matrix, "som": som, "Gemiddelde": gemiddelde, "Aantal even getalen": teller_pos, "Aantal oneven getalen":teller_kwa}

    return thisdict


matrix = [[2, 3, -4], [6, -7, 8], [1, -5]]
resultaat = nested_lst(matrix)
print(resultaat)
