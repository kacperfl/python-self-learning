# Schrijf functie gemiddelde(), die de gebruiker vraagt 
# om een willekeurige zin in te voeren. De functie geeft 
# vervolgens de gemiddelde lengte van de woorden in de zin als returnwaarde terug. 
# Test je code door de methode aan te roepen en het resultaat te printen.


def gemiddelde():
    zin = input("Voer een zin in: ").strip()
    splited = zin.split()
    gemiddelde_waarde = len(zin) / len(splited)
    print(gemiddelde_waarde)

gemiddelde()