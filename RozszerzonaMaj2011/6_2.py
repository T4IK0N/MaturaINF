with open("materialy/liczby.txt", "r") as f:
    lines_binarne = [line.strip() for line in f.readlines()]
    lines_dziesietne = []
    najwieksza_dziesietnie = 0
    najwieksza_binarnie = ""

    for binarna in lines_binarne:
        dziesietna=0
        for i in range(len(binarna)):
            dziesietna += 2 ** i * int(binarna[len(binarna) - i - 1])
        lines_dziesietne.append(dziesietna)

        if dziesietna > najwieksza_dziesietnie:
            najwieksza_dziesietnie=dziesietna
            najwieksza_binarnie = binarna

    # print(lines_binarne)
    # print(lines_dziesietne)
    print(najwieksza_dziesietnie, najwieksza_binarnie)