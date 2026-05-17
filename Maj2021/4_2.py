import string

with open("materialy\\instrukcje.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    n = len(lines)

    lista_dopisz = []
    lista_usun = []
    lista_przesun = []
    lista_zmien = []
    for i in range(n):
        komenda = lines[i][:(lines[i].rfind(" "))] #np. DOPISZ, USUN
        if komenda == "DOPISZ":
            lista_dopisz.append(i)
        if komenda == "USUN":
            lista_usun.append(i)
        if komenda == "PRZESUN":
            lista_przesun.append(i)
        if komenda == "ZMIEN":
            lista_zmien.append(i)

    czego = ""
    najwieksza_ilosc = 0
    ilosc = 0
    for i in range(len(lista_dopisz)-1):
        if lista_dopisz[i+1] - lista_dopisz[i] == 1:
            ilosc += 1
        else:
            ilosc += 1
            if ilosc > najwieksza_ilosc:
                czego = "DOPISZ"
                najwieksza_ilosc = ilosc
            ilosc = 0

    for i in range(len(lista_usun)-1):
        if lista_usun[i+1] - lista_usun[i] == 1:
            ilosc += 1
        else:
            ilosc += 1
            if ilosc > najwieksza_ilosc:
                czego = "USUN"
                najwieksza_ilosc = ilosc
            ilosc = 0

    for i in range(len(lista_przesun)-1):
        if lista_przesun[i+1] - lista_przesun[i] == 1:
            ilosc += 1
        else:
            ilosc += 1
            if ilosc > najwieksza_ilosc:
                czego = "PRZESUN"
                najwieksza_ilosc = ilosc
            ilosc = 0

    for i in range(len(lista_zmien)-1):
        if lista_zmien[i+1] - lista_zmien[i] == 1:
            ilosc += 1
        else:
            ilosc += 1
            if ilosc > najwieksza_ilosc:
                czego = "ZMIEN"
                najwieksza_ilosc = ilosc
            ilosc = 0

    print(czego, najwieksza_ilosc)