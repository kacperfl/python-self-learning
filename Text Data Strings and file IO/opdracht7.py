zin = "  Hallo wereld! Dit is een test.  "

aangepaaste_versie = zin.strip().lower()
woord_aanpassen = aangepaaste_versie.replace("test", "oefening").split()

x = "-".join(woord_aanpassen)
print(x)
