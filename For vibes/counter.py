zin = input("Voer een string in: ").strip().lower()
lst = []
teller = 0

for woord in zin.split():
    if len(woord) > 4:
        teller += 1
        lst.append(woord)

print(f"aantal woorden waar van de letters grooter zijn dan vier is: {teller} en de lijst met dat worden is {lst}")
        