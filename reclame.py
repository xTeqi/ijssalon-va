## Imports
from algemene_functies import mijn_functie_2

## Aanbieding 1
def aanbieding_1(smaak, prijs, korting):
    prijs_na_korting = prijs * (1 - korting)
    return f"Vandaag in de aanbieding: Emmertje ijs (1 liter) in de smaak {smaak}, van €{prijs:.2f} voor €{prijs_na_korting:.2f} euro."
print(aanbieding_1("aardbei",4,0.1))