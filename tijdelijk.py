prijzen = {
    "aardbei" : "3",
    "vanille" : "4",
    "chocolade" : "5"
}

aanbieding = (float(prijzen["aardbei"]) * 0.8)

reclame_tekst = (f"Vandaag in de aanbieding: aardbei-ijs, 1 liter – slechts € {aanbieding}")
reclame_tekst2 = reclame_tekst[:63]

print (reclame_tekst2)