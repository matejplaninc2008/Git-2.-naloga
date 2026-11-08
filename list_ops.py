seznam = [12, 5, 8, 21, 3, 16, 9, 14]

def sestevek():
    vsota = 0
    for i in range(len(seznam)):
        vsota += seznam[i]
    return vsota

def povprecje(seznam):
    rezultat = sum(seznam) / len(seznam)
    return rezultat