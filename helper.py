def decoreer(tekst=""):
    lengte = len(tekst) + 4
    print()

    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()
    
def fooi_pp(bedrag,personen):
    bedrag_pp = bedrag / personen
    return (f"Het bedrag per persoon is {bedrag_pp} euro.")

def onderstreep(tekst=""):
    uit = []
    uit.append(tekst)
    uit.append(len(tekst) * "=")
    return uit      

def bereken_totaal(inkomsten):
    totaal = 0
    for item, bedrag in inkomsten.items():
        totaal += bedrag  # Tel elke waarde op bij het totaal
    return totaal  # Geef het totaal terug na de loop