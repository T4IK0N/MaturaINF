with open("materialy/symbole.txt") as f:
    lines = [line.strip() for line in f.readlines()]

    char='*'
    pozycje_pierwszy = []
    pozycje_drugi = []
    pozycje_trzeci = []
    ilosc_kwadratow = 0
    for y in range(3):
        for i in range(len(lines)-2):
            pozycje_pierwszy = []
            pozycje_drugi = []
            pozycje_trzeci = []
            for x in range(3):
                for j in range(12):
                    if lines[i+x][j] == char:
                        if x == 0:
                            pozycje_pierwszy.append(j)
                        elif x == 1:
                            pozycje_drugi.append(j)
                        elif x == 2:
                            pozycje_trzeci.append(j)

            # print(lines[i])

            pozycje_pierwszy.extend([999]*(12-len(pozycje_pierwszy)))
            pozycje_drugi.extend([999]*(12-len(pozycje_drugi)))
            pozycje_trzeci.extend([999]*(12-len(pozycje_trzeci)))
            # print(pozycje_pierwszy)
            # print(pozycje_drugi)
            # print(pozycje_trzeci)
            pozycje_wybrane = []

            for k in range(12):
                if pozycje_pierwszy[k] == 999: continue
                if pozycje_pierwszy[k] in pozycje_drugi and pozycje_pierwszy[k] in pozycje_trzeci:
                    pozycje_wybrane.append(pozycje_pierwszy[k])

            pozycje_wybrane.sort()
            for k in range(len(pozycje_wybrane)-2):
                if pozycje_wybrane[k]+2 == pozycje_wybrane[k+1]+1 == pozycje_wybrane[k+2]:
                    ilosc_kwadratow+=1
                    # print("ilosc kwadratow:",ilosc_kwadratow)
                    print("srodkowe pole na pozycji: ",pozycje_wybrane[k+1]+1)
                    print("srodkowe pole w wierszu: ", i+2)
            # print(pozycje_wybrane, char)

        if y == 0:
            char='+'
        if y == 1:
            char='o'

    print("ilosc kwadratow: ", ilosc_kwadratow)