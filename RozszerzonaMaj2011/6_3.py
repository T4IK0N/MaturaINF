with open("materialy/liczby.txt", "r") as f:
    lines_binarne = [line.strip() for line in f.readlines()]
    lines_dziesietne = []
    ile_liczb = 0
    suma_liczb_dziesietnie = 0

    for binarna in lines_binarne:
        dziesietna=0
        for i in range(len(binarna)):
            dziesietna += 2 ** i * int(binarna[len(binarna) - i - 1])
        lines_dziesietne.append(dziesietna)

        if len(binarna) == 9:
            ile_liczb += 1
            suma_liczb_dziesietnie += dziesietna

    print(ile_liczb)
    print(bin(suma_liczb_dziesietnie))