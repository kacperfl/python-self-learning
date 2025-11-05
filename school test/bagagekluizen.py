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


def kluis_openen(data):
    ask_kluisnr = int(input("Voer de kluis nummer in: "))
    ask_password = input("Voer de wachtwoord in voor de kluis nummer: ").strip()
    with open(data, "r") as file:
        for regel in file:
            regel = regel.strip()
            regel = regel.split(";")
            kluis_nr = int(regel[0])
            wachtwoord = regel[1]
            if ask_kluisnr == kluis_nr:
                if ask_password == wachtwoord:
                    return True, ask_kluisnr, ask_password
        else: 
            return False, None

def kluis_teruggeven(data):
    resultaat, nummer, password = kluis_openen("kluizen.txt")   
    if resultaat == False:
        return False
    elif resultaat == True:
        regels = []
        with open(data, "r") as read:
            for regel in read:
                regel = regel.strip()
                regel = regel.split(";")
                kluis_nr = int(regel[0])
                if kluis_nr != nummer:
                    regels.append(regel)
            
            with open(data, "w") as remove:
                for waarde in regels:
                    num = waarde[0]
                    wachtwoord = waarde[1]
                    remove.write(f"{num};{wachtwoord} \n")
    return True
        
while True:
    print(50 * "=")
    print("1: Ik wil weten hoeveel kluizen nog vrij zijn ")
    print("2: Ik wil een nieuwe kluis")
    print("3: Ik wil even iets uit mijn kluis halen")
    print("4: Ik geef mijn kluis terug")
    print("5: Stop met het programma")
    print(50 * "=")
    
    try: 
        user_menu_option = int(input("Kies uit het menu (1-5): "))
        
    except ValueError:
        print("Foute invoer probeer nog eens")
        
    bestand_info = "kluizen.txt"
    match user_menu_option:
        case 1:
            print(aantal_kluizen_vrij(bestand_info))
        case 2:
            print(nieuwe_kluis(bestand_info))
        case 3:
            print(kluis_openen(bestand_info))
        case 4:
            print(kluis_teruggeven(bestand_info))
        case 5:
            break
    


