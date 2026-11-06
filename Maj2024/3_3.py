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

def nwd(a, b):
    while b != 0:
        if a > b:
            a = a-b
        else:
            b = b-a
    return a

with open("materialy/skrot2.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

    for line in lines:
        if nwd(int(line), nieparzyste(int(line))) == 7:
            print(int(line))