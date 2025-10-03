# Kies drie variabelen a, b, c met willekeurige waarden (mag jezelf verzinnen).

# Maak vier aparte berekeningen en sla ze op in variabelen:

# Een waarin je optellen, vermenigvuldigen en modulo tegelijk combineert, met haakjes om de volgorde te bepalen.

# Een waarin je een gehele deling (//) en een gewone deling (/) in dezelfde formule gebruikt.

# Een waarin je eerst een verschil neemt en dat daarna nog eens met een macht (**) berekent.

# Een waarin je een eerdere berekening van stap 2 gebruikt en die nog verder verwerkt (bijvoorbeeld er opnieuw modulo of deling op toepassen).

# Print alle vier de resultaten in duidelijke zinnen met f-strings, zodat je meteen ziet welke berekening wat doet.

a = 3
b = 12
c = 34

berekening_nr1 = (b + c) * c % b
berekening_nr2 = (c // b) / a
berekening_nr3 = (b - c) ** a
berekening_nr4 = berekening_nr2 / b

print(f"De berekening van som 1 is: {berekening_nr1}, van de som 2: {berekening_nr2:.2f}, van de som 3 waarbij het negatief getal is: {berekening_nr3}, en als laatste som 4: {berekening_nr4:.4f}")

















