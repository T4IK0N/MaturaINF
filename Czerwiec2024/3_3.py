#abcdefghijklmnopqrstuvwxyz

with open("d:\\programowanie\\inf_matura\\Czerwiec2024\\materialy\\slowa.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    slowa = ""

    for index, slowo in enumerate(lines):
        slownik = {}
        for j in range(len(slowo)):
            slownik[slowo[j]] = 0
        for j in range(len(slowo)):
            slownik[slowo[j]] += 1

        najwieksza = 0
        for i in slownik.keys():
            if slownik[i] > najwieksza:
                najwieksza = slownik[i]
        if najwieksza >= len(slowo) / 2:
            slowa += slowo + '\n'

    print(slowa)