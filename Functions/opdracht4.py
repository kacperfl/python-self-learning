# Maak twee functies:

# Functie A: neemt één getal als parameter en vermenigvuldigt het met 2.

# Functie B: neemt één getal als parameter en telt er 10 bij op.

# Roep beide functies zo aan dat je eerst Functie A gebruikt en het resultaat daarvan gebruikt als input voor Functie B.

# Print het eindresultaat.


def vermenigvuldigen(invoer):
    return invoer * 2

def optellen(getal):
    return getal + 10

inputUser = int(input("Voer een getal in: "))
resultaat1 = vermenigvuldigen(inputUser) 
total = optellen(resultaat1)

print(total)