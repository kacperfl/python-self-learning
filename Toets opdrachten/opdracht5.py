# Schrijf een functie magStemmen(leeftijd, heeftID) die:

# True teruggeeft als de persoon 18 jaar of ouder is én heeftID == True

# anders False teruggeeft.

def magStemmen(leeftijd, heeftID):
    if leeftijd >= 18 and heeftID == "ja":
       return True
    else:
       return False
    

print(magStemmen(18, "nee"))
    