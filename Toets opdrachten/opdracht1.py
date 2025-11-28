# Laat de gebruiker een woord invoeren.
# Print daarna het woord opnieuw, maar met elke letter verdubbeld.
# Bijv. invoer: kat → uitvoer: kkaatt


user_str = input("Voer een string in: ")
resultaat = ""

for i in user_str:
    resultaat = i + resultaat
print(resultaat)
