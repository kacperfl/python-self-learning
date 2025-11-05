# print("1: Ik wil weten hoeveel kluizen nog vrij zijn ")
# print("2: Ik wil een nieuwe kluis")
# print("3: Ik wil even iets uit mijn kluis halen")
# print("4: Ik geef mijn kluis terug")


def aantal_kluizen_vrij(data):

    with open(data, "r") as file:
        alle_kluizen_opslag = 12
        aantal_bezet_kluizen = 0
        for _ in file:
            aantal_bezet_kluizen += 1
        vrije_kluizen = alle_kluizen_opslag - aantal_bezet_kluizen
        return vrije_kluizen


def nieuwe_kluis(bestand):
    vrije_kluiuzen = aantal_kluizen_vrij("kluizen.txt")
    bezete_kluizen = []
    
    if vrije_kluiuzen == 0:
        return -2
    
    user_input = input("Voer een koppel code voor de beschikbaare kluis: ")
        
    if len(user_input.strip()) < 4 or ";" in user_input:
        return -1
    

    with open(bestand, "r") as file:
        for regel in file:
            regel = regel.strip()
            regel = regel.split(";")
            kluis_nr = int(regel[0])
            kluis_code = regel[1] # wordt niet gebruikt maar voor overzichtelijkheid
            bezete_kluizen.append(kluis_nr)

        for num in range(1, 13):
            if num not in bezete_kluizen:
                kleinste_vrije = num
                break

        with open(bestand, "a") as edit:
            edit.write(f"\n{kleinste_vrije};{user_input}")

    return kleinste_vrije


# print(aantal_kluizen_vrij("kluizen.txt"))
print(nieuwe_kluis("kluizen.txt"))
