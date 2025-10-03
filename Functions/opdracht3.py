# Wat je moet doen:

# Maak een functie die drie parameters krijgt: twee getallen en een teken (+, -, * of /).

# Laat de functie afhankelijk van het teken de juiste berekening uitvoeren (optellen, aftrekken, vermenigvuldigen, delen) en het resultaat teruggeven.

# Roep de functie meerdere keren aan met verschillende getallen en tekens, en print de resultaten.

# 💡 Tip: gebruik if/elif/else binnen de functie om te checken welk teken er is.


def calc(getal1, teken, getal2):
    while True:
     if teken != "+" and teken != "-" and teken != "*" and teken != "/":
        print("U heeft geen teken gebruikt probeer nog eens")
        teken = input("Voer nog maals een teken uit")
     else:
        break
    if getal2 == 0:
        print("Je kan niet delen door 0 probeer nog eens")
        getal2 = int(input("Voer een getal uit: "))
    elif teken == "+":
        som = getal1 + getal2
        return som
    elif teken == "-":
        som = getal1 - getal2
        return som
    elif teken == "*":
        som = getal1 * getal2
        return som
    elif teken == "/":
        som = getal1 / getal2
        return som
    else:
        return "Er is iets mis gegaan"
    
    
    

user1 = int(input("Voer een getal uit: "))
speciaal_teken = input("Voer een uitrekening uit: ")
user2 = int(input("Voer een getal uit: "))

print(f"De resultaat van som {user1} {speciaal_teken} {user2} is {calc(user1, speciaal_teken, user2)}")