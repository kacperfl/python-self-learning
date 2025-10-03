# Schrijf een functie met de naam print_list die een lijst binnenkrijgt.
# De functie moet alle waarden één voor één afdrukken.

def print_list(lijst):
    for cijfer in lijst:
        if cijfer < 0:
         print(cijfer)


lst = [1, -3, 12, 5, 65, 23, 6, -1, 1]
print_list(lst)
