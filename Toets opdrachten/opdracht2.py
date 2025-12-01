# 🔢 Opgave 2 – Grootste verschil

# Laat de gebruiker drie getallen invoeren.
# Print het verschil tussen het grootste en het kleinste getal.
# (Zorg dat je niet van tevoren weet welke volgorde de gebruiker intypt.)
lst = []
for i in range(1, 4):
    user_int = int(input(f"Voer een getal {i} uit: " ))
    lst.append(user_int)
som = max(lst) - min(lst)
print(som)
    
    