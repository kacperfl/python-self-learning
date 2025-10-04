# Maak een derde lijst met alleen de oneven getallen.

# Bereken het kwadraat van elk getal in de even lijst.

# Bereken de dubbelwaarde (x2) van elk getal in de oneven lijst.

# Return de even-kwadraat-lijst, de oneven-dubbel-lijst, en het gemiddelde van alle getallen (originele lijst).


def evenOneven(lst_num):
    even_lijst = []
    oneven_lijst = []
    
    for nummer in lst_num:
        if nummer % 2 == 0:
            kwadraat = nummer ** 2
            even_lijst.append(kwadraat)
        else:
            plus = nummer + nummer
            oneven_lijst.append(plus)
    gemiddelde = sum(lst_num) / len(lst_num)
    return even_lijst, oneven_lijst, gemiddelde


lijst = [2, 3, 4, 5, 6]
resultaat = evenOneven(lijst)
print(f"De kwadraat van lijst even is: {resultaat[0]}\n de dubbele van oneven lijst is: {resultaat[1]}\n en de gemiddelde van orginele lijst is: {resultaat[2]}\n")