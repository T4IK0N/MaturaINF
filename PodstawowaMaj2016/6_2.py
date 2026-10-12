def czy_pierwsza(n):
    i=2
    if n == 1 or n == 0:
        return False

    while i!=n:
        if n%i == 0:
            return False
        else:
            i+=1
    return True

with open("materialy/dane6.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    najmniejsza = 1000
    najwieksza = 0

    for line in lines:
        if czy_pierwsza(int(line)):
            if int(line) > najwieksza:
                najwieksza = int(line)
            if int(line) < najmniejsza:
                najmniejsza = int(line)

    print(najmniejsza)
    print(najwieksza)