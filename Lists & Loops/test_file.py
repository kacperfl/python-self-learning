import math

x1 = int(input("X positie van cordintaat 1: "))
y1 = int(input("Y positie van cordintaat 1: "))
x2 = int(input("X positie van cordintaat 2: "))
y2 = int(input("Y positie van cordintaat 2: "))

afstand = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(f"Asftand tussen cordinaat 1 {(x1, x2) ** 2} en {y1, y2} is {afstand:.4f}")