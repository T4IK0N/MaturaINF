#liczba1 < liczba2
def czy_jest_wielokrotnością(liczba1, liczba2):
    if liczba1 is None or liczba2 is None: return False
    if liczba2 == liczba1: return False #bo to bedzie 1
    return liczba2 % liczba1 == 0

#tylko trojki
with open("d:\\programowanie\\inf_matura\\Maj2022\\materialy\\liczby.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    lista_trojek = []
    lista_piatek = []
    ilosc_trojek = 0
    ilosc_piatek = 0

    for a in range(len(lines)):
        pierwsza = int(lines[a])
        for b in range(len(lines)):
            druga = int(lines[b])
            if czy_jest_wielokrotnością(pierwsza, druga):
                for c in range(len(lines)):
                    trzecia = int(lines[c])
                    if czy_jest_wielokrotnością(druga, trzecia):
                        lista_trojek.append(f"{pierwsza} {druga} {trzecia}\n")
                        ilosc_trojek+=1
                        for d in range(len(lines)):
                            czwarta = int(lines[d])
                            if czy_jest_wielokrotnością(trzecia, czwarta):
                                for e in range(len(lines)):
                                    piata = int(lines[e])
                                    if czy_jest_wielokrotnością(czwarta, piata):
                                        lista_piatek.append(f"{pierwsza} {druga} {trzecia} {czwarta} {piata}\n")
                                        ilosc_piatek += 1
    with open("d:\\programowanie\\inf_matura\\Maj2022\\materialy\\trojki.txt", "w") as w:
        w.writelines(lista_trojek)
    print(ilosc_trojek, "(trójki)")
    print(ilosc_piatek, "(piątki)")