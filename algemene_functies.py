def mijn_functie_1(a):
    return a * a
print(mijn_functie_1(12))

def mijn_functie_2(a,b):
    mijn_functie_2_list = []
    mijn_functie_2_list.append(a + b)
    mijn_functie_2_list.append(a - b)
    mijn_functie_2_list.append(a * b)
    mijn_functie_2_list.append(a // b)
    return mijn_functie_2_list
print(mijn_functie_2(12,3))