# Lezen
with open("kaartnummer.txt", "r") as infile:
    inhoud = infile.read()

# Bewerken in geheugen (bijvoorbeeld alles uppercase)
nieuwe_inhoud = inhoud.upper()

# Schrijven
with open("output.txt", "w") as outfile:
    outfile.write(nieuwe_inhoud)
