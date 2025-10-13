import random

counter = 0
totaal = 0

while True:
    random_int = random.randint(1, 20)
    if totaal > 100:
        print(f"de totaal waarden is {totaal} en het aantal getalen dat opgeteld waren zijn: {counter}")
        break
    
    totaal += random_int
    counter += 1 
        
