def maak_nette_zin(invoer):
    invoer = invoer.strip()
    invoer = " ".join(invoer.split())
    invoer = invoer.lower()
    invoer = invoer.capitalize()
    if not invoer.endswith("."):
        invoer += "."
    return invoer
        
        
zin = "   DIt  IS   eEN  TESTzin  "
print(maak_nette_zin(zin))
    