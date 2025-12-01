# Vraag de gebruiker een woord in te voeren.

# Check of het woord hetzelfde is als het omgekeerde.

# Print "Ja, een palindroom!" of "Nee, geen palindroom."

user = input("Voer een zin in: ")
omgekeerd = ""

for letter in user:
    omgekeerd = letter + omgekeerd
    
    
if omgekeerd == user:
    print("Ja, een palindroom!")
else:
    print("Nee, geen palindroom.")
