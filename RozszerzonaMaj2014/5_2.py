with open("materialy/NAPIS.TXT") as f:
    lines = [line.strip() for line in f.readlines()]

    wartosci_ascii = []
    for line in lines:
        pomocnicza = []
        for letter in line:
            pomocnicza.append(ord(letter))
        wartosci_ascii.append(pomocnicza)


    rosnace = []
    for i in range(len(wartosci_ascii)):
        czy_rosnacy = True
        for j in range(len(wartosci_ascii[i])-1):
            if wartosci_ascii[i][j] > wartosci_ascii[i][j+1]:
                czy_rosnacy = False
        if czy_rosnacy:
            rosnace.append(lines[i])
    print("\n".join(rosnace))