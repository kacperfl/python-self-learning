tekst = "Hallo hallo wereld wereld wereld test test oefening".lower()

telling = {}


for i in tekst.split():
    if i not in telling:
        telling[i] = 1
    else:
        telling[i] += 1
print(telling)
     
