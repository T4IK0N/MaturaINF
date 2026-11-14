with open("materialy/mapa.txt", "r") as f:
    lines = [line.split() for line in f.readlines()]

    najwieksza, i = 0, 0
    for index, line in enumerate(lines):
        if int(line[2]) > najwieksza:
            najwieksza = int(line[2])
            i = index
    print(i+1, najwieksza)