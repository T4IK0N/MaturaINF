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

j = 39101
print(nieparzyste(j))