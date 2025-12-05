#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Oriëntatie op AI

Oefening: Lineaire regressie

(c) 2023 Hogeschool Utrecht,
Peter van den Berg (petervandenberg@hu.nl)


Let op! Het is niet toegestaan om bestaande modules te importeren en te
        gebruiken, zoals `math` en `statistics`.
"""


def gradient_descent(x, y, num_iterations=1000, learning_rate=0.0001):
    a = 0
    b = 0
    n = len(x)
    
    
    for _ in range(num_iterations):
        gradient_a = 0
        gradient_b = 0
        
        for xi, yi in zip(x, y):
            #in wiskunde is het anders:
            # y_pred = (a * x) + b
            # error = y - y_pred
            error = (a + b * xi) - yi
            gradient_a += 2 * error    
            gradient_b += 2 * error * xi
            
        a -= gradient_a * learning_rate / n
        b -= gradient_b * learning_rate / n
        
    return [a, b]

"""
==========================[ HU TESTRAAMWERK ]================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""


def __my_assert_args(function, args, expected_output, check_type=True):
    """
    Controleer of gegeven functie met gegeven argumenten het verwachte resultaat oplevert.

    Optioneel wordt ook het return-type gecontroleerd.
    """
    argstr = str(args).replace(',)', ')')
    output = function(*args)

    # Controleer eerst het return-type (optioneel)
    if check_type:
        msg = f"Fout: {function.__name__}{argstr} geeft geen {type(expected_output)} terug als return-type"
        assert type(output) is type(expected_output), msg

    # Controleer of de functie-uitvoer overeenkomt met de gewenste uitvoer
    msg = f"Fout: {function.__name__}{argstr} geeft {output} in plaats van {expected_output}"
    is_float = type(expected_output) is float
    is_float_list = type(expected_output) is list and all([type(item) is float for item in expected_output])
    if is_float:
        # Vergelijk bij float als return-type op 7 decimalen om afrondingsfouten te omzeilen
        assert round(output - expected_output, 7) == 0, msg
    elif is_float_list:
        # Vergelijk bij floatlijst als return-type op 7 decimalen om afrondingsfouten te omzeilen
        assert [round(x - y, 7) for x, y in zip(output, expected_output)] == [0.0] * len(output), msg
    else:
        assert output == expected_output, msg


def test_gradient_descent():    
    data = {
        'presence': [29, 36, 41, 45, 48, 50, 56, 61, 67, 67, 67, 71, 75, 79, 83, 88],
        'grade': [4.1, 4.3, 4.0, 5.2, 4.8, 4.9, 5.9, 5.2, 4.9, 5.7, 6.2, 6.1, 4.4, 6.1, 6.8, 6.9]
    }

    testcases = [
        ((data['presence'], data['grade'], 1), [0.00106875, 0.06671125]),
        ((data['presence'], data['grade'], 10), [0.0017250805547328813, 0.0853495859860294]),
        ((data['presence'], data['grade'], 100), [0.005413509270166133, 0.0852927847242298]),
        ((data['presence'], data['grade'], 1000), [0.042033257409484846, 0.08472863642441471]),
        ((data['presence'], data['grade'], 10000), [0.38301565829600587, 0.0794756062562346]),
        ((data['presence'], data['grade'], 100000), [2.1618476839980865, 0.052071674936483736]),
        ((data['presence'], data['grade'], 524288), [2.8178099369653586, 0.041966198832538895]),
    ]

    for case in testcases:
        __my_assert_args(gradient_descent, case[0], case[1])
    return 1


def __main():
    try:
        print("\x1b[32m")

        test_gradient_descent()
        print("Je functie gradient_descent() werkt goed!")

    except AssertionError as ae:
        print("\x1b[31m")   # Rode tekstkleur
        if not ae:
            print("Je code veroorzaakt onderstaande AssertionError:")
            raise ae
        else:
            print(ae)
        print("\x1b[0m")    # Reset tekstkleur


if __name__ == '__main__':
    __main()