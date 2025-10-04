# Je krijgt een 2D-lijst (matrix) met willekeurige getallen.
# Doel: maak een functie die:

# Alle even getallen verdubbelt,

# Alle oneven getallen vervangt door hun kwadraat,

# Alle negatieve getallen verwijdert (dus ze tellen nergens mee),

# De functie moet twee waarden teruggeven:

# De nieuwe matrix (met bewerkte getallen)

# De som van alle bewerkte waarden samen

# 💡 Hint 1: Je hebt dus een dubbele for-loop nodig (om door rijen en getallen te lopen).
# 💡 Hint 2: Let op — je moet een nieuwe matrix bouwen, niet in de oude lijst aanpassen.
# 💡 Hint 3: Som kun je pas berekenen nadat de hele nieuwe matrix klaar is.


def nested_lst(lijst):
    nieuwe_matrix = []

    for rij in lijst:
        nieuwe_rij = []
        for num in rij:
            if num < 0:
                continue
            elif num % 2 == 0:
                verdubbelen = num * 2
                nieuwe_rij.append(verdubbelen)
            elif num % 2 > 0:
                kwadraat = num ** 2
                nieuwe_rij.append(kwadraat)
        nieuwe_matrix.append(nieuwe_rij)

    som = 0
    for reeks in nieuwe_matrix:
        totaal = sum(reeks)
        som += totaal

    return nieuwe_matrix, som


matrix = [[2, 3, -4], [6, -7, 8], [1, -5]]
resultaat = nested_lst(matrix)
print(f"De nieuwe matrix is: {resultaat[0]} en som is {resultaat[1]}")
