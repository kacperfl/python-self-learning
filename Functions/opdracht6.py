# Maak een functie die een lijst van getallen als parameter krijgt.

# Laat de functie door elk getal in de lijst lopen (gebruik een loop).

# Voor elk getal:

# Als het getal even is, vermenigvuldig het met 2.

# Als het getal oneven is, tel er 5 bij op.

# De functie moet een nieuwe lijst teruggeven met de aangepaste getallen.

# Roep de functie aan met een testlijst van minstens 7 getallen en print het resultaat.

def uitwerken(lijst):
    getalen_lijst = []
    for i in lijst:
        if i % 2 == 0:
            i *= 2
        elif i % 2 > 0:
            i += 5
        getalen_lijst.append(i)
    return getalen_lijst
            
lst = [12, 23, 2, 8, 6, 2, -2, 1,15]
resultaat = uitwerken(lst)

print(f"De nieuwe lijst is: {resultaat}")