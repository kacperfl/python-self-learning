# Opgave 4 – Oneven getallen optellen

# Laat de gebruiker getallen invoeren tot hij “stop” typt.
# Tel alleen de oneven getallen bij elkaar op en print de som.
# (Hint: gebruik % 2 != 0 en een while loop.)
lst = []

while True:
    user_input = input("Voer een getal in of zeg stop: ")
    if user_input == "stop":
        break

    number = int(user_input)

    if number % 2 != 0:
        lst.append(number)

# buiten de loop printen:
print(f"Dit is de som van uw invoer: {sum(lst)}")
