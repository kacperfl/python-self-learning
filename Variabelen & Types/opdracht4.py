# Opdracht:

# Vraag de gebruiker om een getal via input() en sla dat op in een variabele getal.

# Zet dat getal om naar een int.

# Maak een variabele kwadraat die het kwadraat van dat getal bevat (dus getal × getal).

# Print een zin als:
# "Het kwadraat van 5 is 25" (maar natuurlijk afhankelijk van wat de gebruiker invult).

user_input = (input("Voer een getal in: "))
int_num = int(user_input)
kwadraat = int_num ** 2

print(f"Het kwadraat van {int_num} is {kwadraat}")