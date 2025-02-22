## Imports
from algemene_functies import mijn_functie_2

## Aanbieding 1
def aanbieding_1(smaak, prijs, korting):
    prijs_na_korting = prijs * (1 - korting)
    return f"Vandaag in de aanbieding: Emmertje ijs (1 liter) in de smaak {smaak}, van €{prijs:.2f} voor €{prijs_na_korting:.2f} euro."
print(aanbieding_1("aardbei",4,0.1))

# Inkomstentotaal per week inclusief btw
def inkomsten_totaal(inkomsten, btw):
    inkomsten_totaal_uitvoer = sum(inkomsten)
    btw_bedrag = sum(inkomsten) * (1 * btw)
    return f"Het totaal van alle inkomsten van deze week is {inkomsten_totaal_uitvoer:.2f} euro, waarover {btw_bedrag:.2f} euro btw betaald moet worden."
print(inkomsten_totaal([220, 430, 125, 160, 205, 90, 345], 0.09))

## Laag en hoog
def laag_en_hoog(mijn_lijst):
    laag = min(mijn_lijst)
    hoog = max(mijn_lijst)
    return [laag, hoog]
print(laag_en_hoog([220, 430, 125, 160, 205, 90, 345]))

## Gemiddelde
def gemiddelde(mijn_lijst):
    gemiddelde_bedrag = sum(mijn_lijst) / len(mijn_lijst)
    return f"De gemiddelde inkomsten deze week zijn {gemiddelde_bedrag:.2f} euro."
print(gemiddelde([220, 430, 125, 160, 205, 90, 345]))

## Meervoudig
def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)
print(meervoudig([10,5,3,2,1,2,9]))

## Combinatie
def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0],korte_lijst[1])
    return uitvoer