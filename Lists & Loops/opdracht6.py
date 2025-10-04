# Je krijgt een lijst van lijsten, waarin elk sub-lijstje een reeks getallen bevat.
# Jouw taak:

# Tel alle getallen bij elkaar op.

# Bereken het gemiddelde van álle getallen samen.

# Maak een nieuwe lijst waarin elk getal wordt verdubbeld.

def loops(lst):
    new_lst = []
    placeholder_lst = []
    #verdubbelde nieuwe lijst
    for rij in lst:
        for cijfer in rij:
            cijfer += cijfer
            new_lst.append(cijfer)
    #somen uitreken in een aparte lijst
    for reeks in lst:
        for num in reeks:
            placeholder_lst.append(num)
        gemiddelde = sum(placeholder_lst) / len(placeholder_lst)
        som = sum(placeholder_lst)
    
    return new_lst, som, gemiddelde

matrix = [[2, 3, 4], [6, 7, 8], [1, 5]]
resultaat = loops(matrix)
print(f"De totale som is: {resultaat[1]}")
print(f"De gemiddelde waarde van de lijst is: {resultaat[2]}")
print(f"De verdubbelde waarde van de lijst is: {resultaat[0]}")