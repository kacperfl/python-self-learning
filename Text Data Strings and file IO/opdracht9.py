user = input("Voer een string in: ")
zin = user.strip().lower()
telling = {}

woorden = zin.split()
for woord in woorden:
    if woord not in telling:
        telling[woord] = 1
    else:
        telling[woord] += 1

teller = max(telling.values())
print(f"Het meest voorkomende woord is {max(telling, key=telling.get)} en komt {teller} voor")

