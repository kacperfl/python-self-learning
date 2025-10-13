zin = "  Hallo wereld! Dit is een test.  "

aangepaaste_versie = zin.strip().lower()
splited = aangepaaste_versie.split()
   
aantal = len(splited)

print(f"De lijst: {splited} en de aantal woorden: {aantal}")