# Verwijder alle overbodige spaties aan het begin en einde.

# Vervang het woord "super" door "echt".

# Splits de zin in woorden en voeg ze daarna weer samen met één enkele spatie.

# Zorg dat de eerste letter van de zin een hoofdletter is.

# Print de uiteindelijke nette zin.

zin = "   python is   super leuk   "
zin = zin.strip()
zin = zin.replace("super", "echt")
zin = zin.split()
zin = " ".join(zin)
zin = zin.capitalize()


print(zin)