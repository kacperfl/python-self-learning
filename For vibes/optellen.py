import random

counter = 0
totaal = 0
lst = []
while True:
    if totaal > 100:
        print(f"de totaal waarden is {totaal} met de alle nummers: {lst} en het aantal getalen dat opgeteld waren zijn: {counter}")
        break
    
    random_int = random.randint(1, 20)
    lst.append(random_int)
    totaal += random_int
    counter += 1 
        
