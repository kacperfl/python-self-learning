import random

prijs = random.randint(10, 150)

betaald = int(input("Voer het bedrag in eurocent in dat je betaalt: "))

wisselgeld = betaald - prijs

print(f"\nDe prijs van het gekozen product: {prijs}")
print(f"Het betaalde bedrag: {betaald}\n")

munten = [50, 20, 10, 5, 2, 1]

for munt in munten:
    aantal = wisselgeld // munt       
    wisselgeld = wisselgeld % munt  
    print(f"aantal munten van {munt} eurocent is {aantal}")
