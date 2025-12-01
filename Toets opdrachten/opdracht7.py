# De gebruiker typt getallen totdat hij “stop” zegt.

# Het programma berekent daarna het gemiddelde van alle getallen.

# Tips voor structuur:

# Start met een lege lijst of teller/som-variabelen.

# Gebruik while True: voor de loop.

# Vraag input binnen de loop.

# Stop de loop met break als de gebruiker “stop” typt.

# Tel de getallen op en houd bij hoeveel er zijn.

# Bereken buiten de loop het gemiddelde (som / aantal) en print het, afgerond op 2 decimalen.

totaal = 0
teller = 0
while True:
    user_input = input("Voer een getal in of zeg stop: ")
    
    if user_input != "stop":
        number = int(user_input)
        totaal += number
        teller += 1
    else:
        break
gemiddelde = totaal / teller
print(f"De gemiddelde van invoer is {gemiddelde:.2f}")