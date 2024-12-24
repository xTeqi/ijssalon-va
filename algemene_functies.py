basisgetal = 12
modifier = 3

def mijn_functie_1():
    global basisgetal
    return pow(basisgetal,2)
print(f"Functie 1: {mijn_functie_1()}")

def mijn_functie_2():
    global basisgetal
    global modifier
    return [
        basisgetal + modifier, 
        basisgetal - modifier, 
        basisgetal * modifier, 
        basisgetal // modifier
    ]
print(f"Functie 2: {mijn_functie_2()}")