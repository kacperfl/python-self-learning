# Kies drie variabelen a, b, c met willekeurige waarden (bijv. rond 10–20).

# Maak drie aparte berekeningen en sla ze in variabelen op:

# Een berekening waarin je optellen en vermenigvuldigen combineert met een gehele deling.

# Een berekening waarin je modulo gebruikt binnen haakjes, gecombineerd met een vermenigvuldiging of deling.

# Een berekening waarin je een verschil (–) vermenigvuldigt met een som waarin ook een modulo zit.

# Print de resultaten met duidelijke f-strings.

a = 12
b = 17
c = 20

som1 = (a + b) * c // a
som2 = (b % c) * a
som3 = (c - a) * som2 % c

print(f"De resultaat van som 1 is: {som1}, van de som 2: {som2} en van de som 3 is: {som3}")