with open("materialy/liczby.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    ilosc = 0
    liczba = []
    czyWystapila = False
    for i in range(len(lines)):
        if not czyWystapila and lines[i][-1] == lines[i][0]:
            liczba = lines[i]
            czyWystapila = True
        if lines[i][-1] == lines[i][0]:
            ilosc+=1

    print(ilosc, "\n"+"".join(liczba))