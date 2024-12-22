def aanbieding_1(smaak, prijs, korting):
    prijs_na_korting = prijs * (1 - korting)
    prijs_na_korting_format = f"{prijs_na_korting:.2f}".replace('.' , ',')
    uitvoer = f"Vandaag in de aanbieding: Emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} voor {prijs_na_korting_format} euro."
    return uitvoer
print(aanbieding_1("aardbei",4,0.1))

def inkomsten_totaal():
    inkomsten = sum([220,430,125,160,205,90,345])
    btw = inkomsten * 0.09
    inkomsten_overzicht = f"Het totaal van alle inkomsten deze week is {inkomsten} euro, waarover {btw} euro btw betaald dient te worden."
    return inkomsten_overzicht
print(inkomsten_totaal())

def laag_en_hoog():
    mijn_lijst = [220,430,125,160,205,90,345]
    return [
        min(mijn_lijst),
        max(mijn_lijst)
    ]
print (laag_en_hoog())

def gemiddelde():
    mijn_lijst = [220,430,125,160,205,90,345]
    gemiddeld_bedrag = sum(mijn_lijst) / len(mijn_lijst)
    gemiddeld_bedrag_format = f"{gemiddeld_bedrag:.2f}".replace('.' , ',')
    return f"De gemiddelde inkomsten deze week zijn {gemiddeld_bedrag_format} euro."
print (gemiddelde())