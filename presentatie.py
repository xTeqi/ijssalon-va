def toon_inkomsten(inkomsten, totaal):
    for item, bedrag in inkomsten.items():
        print(f"{item}: {bedrag} euro")
    print("==========================")
    print(f"Totaal: {totaal} euro")
