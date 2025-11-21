#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Oriëntatie op AI

Opdracht: algoritmiek

(c) 2025 Hogeschool Utrecht,
Peter van den Berg (peter.vandenberg@hu.nl)

Opdracht:
Beantwoord onderstaande vragen en werk onderstaande functies uit.
Voeg commentaar toe om je code toe te lichten.

Je kunt je functies testen met het gegeven raamwerk door het bestand
uit te voeren (of met behulp van `pytest`, als je weet hoe dat werkt).
Lever je werk in op Canvas als alle tests slagen.

Let op! Het is niet toegestaan om bestaande modules te importeren en te
        gebruiken, zoals `math` en `statistics`.
"""
import sys
import inspect


# TODO: Vul hier je naam, klas en studentnummer in.
naam = "Kacper Flak"
klas = "V1A"
studentnummer = 1906852

"""
1.  Sorteeralgoritme

    Hieronder staat de pseudocode van een sorteeralgoritme:
    1. Startend vanaf het begin van een lijst, vergelijk elk element met zijn volgende buur.
    2. Als het element groter is dan zijn volgende buur, verwissel ze van plaats.
    3. Doorloop zo de lijst tot het eind.
    4. Als er verwisselingen zijn geweest bij stap 2., ga naar stap 1.

    1a. Handmatig toepassen
        Gegeven is de lijst l = [ 4, 3, 1, 2 ]. Geef de waardes die deze
        lijst aanneemt bij álle tussenstappen bij toepassing van
        bovenstaand sorteeralgoritme.
"""
#       TODO: De start getal is index 0 nummer 4 dus in de lijst deze nummer vergelijken we met de buurman aan de rechter kant als de start index grootter is dan buurman verwisselen we de waardens
#             als dat niet zo is dan wordt index 1 gepakt en checkt weer of het grootter is dan buurman. De start index vergelijkt zich zelf met de waardens 
#             tot dat ie helemaal naar rechts is opgeschoven dat is de grootste waarden dus. 
"""

    1b. Implementatie
        Implementeer het sorteeralgoritme in Python in een functie
        hieronder genaamd my_sort(lst).
        Let op: je *moet* de pseudocode volgen!
"""


def my_sort(lst):
    """
    Sorteer gegeven lijst volgens het algoritme zoals beschreven in de pseudocode.

    1. Startend vanaf het begin van een lijst, vergelijk elk element met zijn volgende buur.
    2. Als het element groter is dan zijn volgende buur, verwissel ze van plaats.
    3. Doorloop zo de lijst tot het eind.
    4. Als er verwisselingen zijn geweest bij stap 2., ga naar stap 1.

    Zorg dat de gegeven lijst niet verandert, maar geef een nieuwe, gesorteerde variant van de lijst terug.

    Args:
        lst (list): Een lijst met elementen van gelijk type, bijvoorbeeld gehele getallen.

    Returns:
        list: Een nieuwe, gesorteerde variant van lijst `lst`.
    """
    # een kopie maken van de lijst ik dacht eerst aan new_list = lst maar na wat meer research kwam ik op .copy()
    new_list = lst.copy()
    
    # hier wordt een while true loop gebruikt omdat ik wil lopen zodra waarden verwisseld zijn
    while True:
        # aan het begin maak ik een var verwisseld aan waar de default waarden False is omdat we zo er op gaan checken
        verwisseld = False
        
        # hier is een for loop gebruikt waarbij ik zeg index in range lengte van de geheel new copy lijst - 1 omdat we met indexes werken zonder die - 1 zouden we aan het eind van de lijst 
        # buiten de lijst komen en error krijgen
        for index in range(len(new_list) - 1):
            # de "buur" is de index rechts naast de start index
            buur = index + 1
            # in de if statment zeg ik als de value en geen index grootter is dan de value van de buur dan wordt ten eerste var verwisseld op true gezet en ten tweede worden die values 
            # met elkaar verwisseld van plek, we verwisselen de values dus en niet de indexes zelf
            if new_list[index] > new_list[buur]:
                verwisseld = True
                new_list[index], new_list[buur] = new_list[buur], new_list[index]
            # als de for loop klaar is dan wordt er laatste check gedaan als verwisseld dan gelijk is aan False betekent dat de loop al gesoorteerd is
        if verwisseld == False:
            break 
    # var lst_sorted is dan gelijk aan gesoorteerde lijst en returnen we de gesoorteerde lijst terug
    lst_sorted = new_list
    return lst_sorted


"""
    1c. Best en worst case
        -   Stel je hebt een lijst met de waarden 1, 2 en 3. Bij welke
            volgorde van de waarden in de lijst is het sorteeralgoritme
            het snelste klaar (best-case scenario)?
            Hoeveel vergelijkingen (zoals beschreven in stap 1. van de
            pseudocode) zijn nodig geweest?
"""
#           TODO: De best case scenario zou al gesoorteerd lijst zijn omdat je dan in totaal 2 vergelijking nodig hebt in dit voorbeeld bijv: is 1 > 2? is 2 > 3? 3 is laatste nummer dan stopt de loop
"""


        -   Bij welke volgorde van de waarden in de lijst is het
            sorteeralgoritme het minst snel klaar (worst-case scenario)?
            Hoeveel vergelijkingen zijn nodig geweest?
"""
#           TODO: De worst case scenario is een lijst van groot naar klein, waarom? We moeten dan de meeste sweeps maken dus het vaakst over de lijst heen lopen om het uit eindelijk te sorteren
"""


        -   Stel je hebt een lijst met de waarden 1 tot en met 4.
            Wat is nu het best-case scenario?
            Hoeveel vergelijkingen zijn er nodig?
            En wat is nu het worst-case scenario?
            Hoeveel vergelijkingen zijn er nodig?
"""
#           TODO: A. Best case scenario: al gesoorteerde lijst
#                 B. Er zijn 3 vergelikingen nodig, omdat is de start index grooter dan buur? nee? oke naar index 1 dan is die grooter dan buur? nee? etc tot aan de eind van de loop
#                 C. Worst-case scenario zou een van groot naar klein oftewel omgekeerde lijst zijn.
#                 D. er zijn 6 vergelijkingen dan nodig de dubbele van de al gesoorteerde lijst, omdat het kijkt is start grootter dan buur waarden? ja? verwissel dat zijn al 2 vergelijkingen, tot je aan de eind loop komt van de lijst dan zijn er 6 vergelijkingen plaats gevonden
"""


        -   (Optioneel) Stel je hebt een lijst met de waarden 1 tot en met n
            (je weet nu dus niet precies hoeveel waarden er in de lijst
            zitten, het zijn er 'n').
            Wat is nu het best-case scenario?
            Hoeveel vergelijkingen zijn er nodig?
            En wat is nu het worst-case scenario?
            Hoeveel vergelijkingen zijn er nodig?
"""
#           TODO: Best case scenario is nog steeds een gesorteerdlijst zoals eerder uitgelegd 
#                 De aantal vergelijkingen is afhankelijk van grootte van de lijst, maar je kan zeggen dat bij best case de aantal vergelijkingen gelijk is aan aantal indexes - 1 omdat index bij 0 begint. n − 1
#                 De worst case is nog steeds omgekeerde lijst
#                 n·(n − 1)/2
"""
"""

"""
2. Linear search recursive
    Implementeer onderstaande functie om element in de gegeven lijst te zoeken door middel van recursief lineair zoeken.
"""


def linear_search_recursive(lst, target):
    """
    Zoek een element in de gegeven lijst door middel van recursief lineair zoeken.

    Zorg dat de inhoud van de gegeven lijst niet verandert.

    Args:
        lst (list):     Een lijst met elementen van gelijk type, bijvoorbeeld gehele getallen.
        target (int):   Het gezochte element.

    Returns:
        bool: Of het element in de lijst voorkomt.
        
    """
    # een if statment om te chekcen of de lijst leeg is, zo wel? dan return Fasle omdat de target niet gevonden kan worden
    if lst == []:
        return False
    # Als de eerste waarden van de lijst gelijk is aan de target dan wordt True geretoneerd
    elif lst[0] == target:
        return True
    # Als de eerste waarde niet de target is, roept de functie zichzelf aan met de rest van de lijst
    # (lst[1:]) totdat de lijst leeg is of de target wordt gevonden.
    else:
        return linear_search_recursive(lst[1:], target)
    



"""
(Optioneel)
3.  Sorteeralgoritme 2

    Hieronder staat de pseudocode van nog een sorteeralgoritme voor een lijst `lst` van natuurlijke getallen:
    1. Bepaal het grootste getal k in de lijst.
    2. Maak een nieuwe lijst van lengte k+1, waarbij elk element in deze tweede lijst begint met de waarde 0.
    3. Tel het aantal voorkomens van elk getal in de originele lijst en sla deze frequentie op in de tweede lijst.
    4. Maak een derde, lege lijst
    5. Voeg elke index van de tweede lijst zo vaak toe aan de derde lijst als zij geteld is in stap 3.
    6. Retourneer de derde lijst: zij is een gesorteerde versie van de originele lijst.

    Implementeer het sorteeralgoritme in Python in een functie
    hieronder genaamd my_sort_2(lst).
    Let op: je *moet* de pseudocode volgen!
"""


def my_sort_2(lst):
    """
    Sorteer gegeven lijst volgens het algoritme zoals beschreven in de pseudocode hierboven.

    Zorg dat de gegeven lijst niet verandert, maar geef een nieuwe, gesorteerde variant van de lijst terug.

    Args:
        lst (list): Een lijst met elementen van gelijk type, bijvoorbeeld gehele getallen.

    Returns:
        list: Een nieuwe, gesorteerde variant van lijst `lst`.
    """
    sorted_lst = []  # stap 4.

    return sorted_lst


"""
==========================[ HU TESTRAAMWERK ]================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""
import random


def __my_assert_args(function, args, expected_output, check_type=True):
    """
    Controleer of gegeven functie met gegeven argumenten het verwachte resultaat oplevert.

    Optioneel wordt ook het return-type gecontroleerd.
    """
    argstr = str(args).replace(",)", ")")
    output = function(*args)

    # Controleer eerst het return-type (optioneel)
    if check_type:
        msg = f"Fout: {function.__name__}{argstr} geeft geen {type(expected_output)} terug als return-type"
        assert type(output) is type(expected_output), msg

    # Controleer of de functie-uitvoer overeenkomt met de gewenste uitvoer
    msg = f"Fout: {function.__name__}{argstr} geeft {output} in plaats van {expected_output}"
    if type(expected_output) is float:
        # Vergelijk bij float als return-type op 7 decimalen om afrondingsfouten te omzeilen
        assert round(output - expected_output, 7) == 0, msg
    else:
        assert output == expected_output, msg


def test_id():
    assert naam != "", "Je moet je naam nog invullen!"
    assert studentnummer != -1, "Je moet je studentnummer nog invullen!"
    assert klas != "", "Je moet je klas nog invullen!"


def test_my_sort():
    lst_test = random.choices(range(-99, 100), k=6)
    lst_copy = lst_test.copy()
    lst_output = my_sort(lst_test)

    assert lst_copy == lst_test, "Fout: my_sort(lst) verandert de inhoud van lijst lst"
    assert lst_output == sorted(
        lst_test
    ), f"Fout: my_sort({lst_test}) geeft {lst_output} in plaats van {sorted(lst_test)}"


def test_linear_search_recursive():
    for _ in range(10):
        lst_test = random.sample(range(20), 6)
        target = random.randrange(20)
        found = target in lst_test
        lst_copy = lst_test.copy()

        outcome = linear_search_recursive(lst_test, target)
        assert (
            lst_copy == lst_test
        ), "Fout: linear_search_recursive(lst, target) verandert de inhoud van lijst lst"
        assert (
            outcome == found
        ), f"Fout: linear_search_recursive({lst_test}, {target}) geeft {outcome} in plaats van {found}"


def test_test_linear_search_recursive_recursiveness():
    limit = sys.getrecursionlimit()
    sys.setrecursionlimit(50)
    try:
        linear_search_recursive(list(range(100)), 100)
        assert False, "Fout: linear_search_recursive werkt niet recursief"
    except RecursionError:
        return
    finally:
        sys.setrecursionlimit(limit)


def test_my_sort_2():
    lst_test = [random.choice(range(10)) for _ in range(10)]
    lst_copy = lst_test.copy()
    lst_output = my_sort_2(lst_test)

    assert (
        lst_copy == lst_test
    ), "Fout: my_sort_2(lst) verandert de inhoud van lijst lst"
    assert lst_output == sorted(
        lst_test
    ), f"Fout: my_sort_2({lst_test}) geeft {lst_output} in plaats van {sorted(lst_test)}"


def __main():
    """Test alle functies."""
    # Noodzakelijk voor gekleurde tekst binnen een Windows terminal
    import os

    os.system("")

    try:
        print("\x1b[32m")  # Groene tekstkleur
        test_id()

        test_my_sort()
        print("Je functie my_sort() werkt goed!")

        test_linear_search_recursive()
        test_test_linear_search_recursive_recursiveness()
        print("Je functie linear_search_recursive() werkt goed!")

        test_my_sort_2()
        print("(Optioneel) Je functie test_my_sort_2() werkt goed!")

        print("\nGefeliciteerd, alles lijkt te werken!")
        print("\x1b[38;5;208m")
        print(
            "Echter, test dit testframework niet of je de pseudocode goed gevolgd hebt."
        )
        print(
            "Ook test dit testframework niet of de juiste antwoorden  bij 1a en 1c hebt gegeven.\x1b[0m"
        )
        print("Controleer die dus nog, en lever dan pas je werk in op Canvas...")

    except AssertionError as ae:
        print("\x1b[31m")  # Rode tekstkleur
        if not ae:
            print("Je code veroorzaakt onderstaande AssertionError:")
            raise ae
        else:
            print(ae)

    print("\x1b[0m")  # Reset tekstkleur


if __name__ == "__main__":
    __main()
