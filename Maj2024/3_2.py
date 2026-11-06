def obroc(k):
    wynik = 0
    while k > 0:
        wynik *= 10
        wynik += k%10
        k //= 10
    return wynik

def nieparzyste(n):
    wynik = 0
    while n > 0:
        if (n%10) % 2 == 0:
            n = n // 10
        else:
            wynik *= 10
            wynik += n%10
            n = n // 10
    m = obroc(wynik)
    return m

with open("materialy/skrot.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

    ilosc = 0
    najwieksza = 0
    for line in lines:
        if nieparzyste(int(line)) == 0:
            ilosc += 1
            if int(line) > najwieksza:
                najwieksza = int(line)
    print(ilosc, najwieksza)