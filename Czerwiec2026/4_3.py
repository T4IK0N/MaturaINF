with open("materialy/mapa.txt", "r") as f:
    lines = [line.split() for line in f.readlines()]

    aglomeracja_bok, aglomeracja_ludnosc = 0, 0
    bok_kwadratu = 250
    while bok_kwadratu > 1:
        powierzchnia_kwadratu = bok_kwadratu ** 2

        suma_ludnosci = 0
        for line in lines:
            wsp_x, wsp_y = int(line[0]), int(line[1])

            if 0 < wsp_x < bok_kwadratu and 0 < wsp_y < bok_kwadratu:
                suma_ludnosci += int(line[2])
        gestosc_zaludnienia = suma_ludnosci / powierzchnia_kwadratu

        if gestosc_zaludnienia > 2:
            aglomeracja_bok = bok_kwadratu
            aglomeracja_ludnosc = suma_ludnosci
            break

        bok_kwadratu -= 1
    print(aglomeracja_bok, aglomeracja_ludnosc)