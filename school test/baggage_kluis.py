# print("1: Ik wil weten hoeveel kluizen nog vrij zijn ")
# print("2: Ik wil een nieuwe kluis")
# print("3: Ik wil even iets uit mijn kluis halen")
# print("4: Ik geef mijn kluis terug")

with open("kluizen.txt", "r") as file:
    for i in file:
        print(i)

def aantal_kluizen_vrij(data):
    for i in enumerate(data, start = 1):
        return f"Er zijn momenteel {i} beschikbaar"
    
    