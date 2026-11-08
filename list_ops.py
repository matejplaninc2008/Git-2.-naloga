seznam = [12, 5, 8, 21, 3, 16, 9, 14]

def sestevek():
    vsota = 0
    for i in range(len(seznam)):
        vsota += seznam[i]
    return vsota

def povprecje(seznam):
    rezultat = sum(seznam) / len(seznam)
    return rezultat

def najvecje(seznam):
    return max(seznam)

def najmanjse(seznam):
    return min(seznam)

def stevilo_sodih(seznam):
    stevec = 0
    for stevilo in seznam:
        if stevilo % 2 == 0:
            stevec += 1
    return stevec

def stevilo_lihih(seznam):
    stevec = 0
    for stevilo in seznam:
        if stevilo % 2 == 1:
            stevec += 1
    return stevec

def uredi_seznam(seznam):
    seznam.sort()
    return seznam

def vecja_od_10(seznam):
    sez[0]
    for stevilo in seznam:
        if stevilo > 10:
            sez.append(stevilo)
    return sez

def dodaj_stevilo(seznam):
    novo = int(input("Vnesi celo število: "))
    seznam.append(novo)
    return seznam
