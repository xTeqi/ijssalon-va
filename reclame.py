## Aanbieding 1
def aanbieding_1(smaak, prijs, korting):
    prijs_na_korting = prijs * (1 - korting)
    return f"Vandaag in de aanbieding: Emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} voor €{prijs_na_korting:.2f} euro."
print (aanbieding_1("aardbei",4,0.1))

#Inkomstentotaal per week inclusief btw
def inkomsten_totaal(inkomsten, btw):
    inkomsten_totaal_uitvoer = sum(inkomsten)
    btw_bedrag = sum(inkomsten) * (1 * btw)
    return f"Het totaal van alle inkomsten van deze week is {inkomsten_totaal_uitvoer:.2f} euro, waarover {btw_bedrag:.2f} euro btw betaald moet worden."
print(inkomsten_totaal([220, 430, 125, 160, 205, 90, 345], 0.09))