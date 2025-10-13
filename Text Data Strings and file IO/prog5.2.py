zin = input("Voer een tekst in: ").strip()

def omzetter(invoer):
 nieuwe_woorden = []
 woorden = invoer.split()
 for woord in woorden:
    if woord[0] in 'aeuoi':
       nieuwe_woord =  "#" + woord
       nieuwe_woorden.append(nieuwe_woord)
    elif len(woord) == 3:
        nieuwe_woord = woord.lower()
        nieuwe_woorden.append(nieuwe_woord)
    elif len(woord) < 4:
        nieuwe_woorden.append(woord.upper())
    else:
        nieuwe_woorden.append(woord + "*")
        
 return nieuwe_woorden

print(' '.join(omzetter(zin)))
