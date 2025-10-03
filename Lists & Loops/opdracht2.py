# Opdracht 2

# Schrijf een functie die een lijst van getallen binnenkrijgt en het volgende doet:

# Creëer een nieuwe lijst waarin:

# elk even getal wordt verdubbeld,

# elk oneven getal 5 erbij krijgt.

# Return de nieuwe lijst.

def uitrekenen(lijst):
    new_lst = []
    for cijfer in lijst:
        if cijfer % 2 == 0:
            verdubbelen = cijfer + cijfer
            new_lst.append(verdubbelen)
        elif cijfer % 2 > 0:
            plus_getal = cijfer + 5
            new_lst.append(plus_getal)
    return new_lst

lst = [1, -3, 12, 5, 65, 23, 6, -1, 1]
print(uitrekenen(lst))