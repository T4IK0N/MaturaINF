import string
with open("materialy\\pary.txt") as f:
    lines = [line.strip() for line in f.readlines()]
    n = len(lines)

    for i in range(n):
        ciag = lines[i][lines[i].find(" ")+1:]

        # print(ciag)
        najwieksza_ilosc = 0
        zapisana_litera = ""
        for j in range(len(ciag)-1):
            ilosc = 1
            k = j
            while ciag[k] == ciag[k+1] and not k+1 == len(ciag)-1:
                ilosc += 1
                k+=1

            if ilosc > najwieksza_ilosc:
                zapisana_litera = ciag[j]
                najwieksza_ilosc = ilosc

        print(zapisana_litera*najwieksza_ilosc, najwieksza_ilosc)