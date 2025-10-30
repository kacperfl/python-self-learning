user = int(input("Voer de aantal minuten in: "))

uur = user // 60
rest = (user % 60) * 60
print(f"{user} minuten is {uur} uur en {rest} seconde")