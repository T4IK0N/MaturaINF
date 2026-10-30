def algorytm(w: int, k: int, n: int) -> int:
    n2 = n
    ile = 0
    dlugosc_tablicy = 0

    while n!=0:
        n //= 2
        ile += 1
        dlugosc_tablicy += 1

    wynik_odwrocony = [0] * ile
    i = 0
    n = n2

    while n != 0:
        wynik_odwrocony[i] = n % 2
        n //= 2
        i += 1

    wynik = [0] * ile
    i = dlugosc_tablicy-1
    while i >= 0:
        wynik[i] = wynik_odwrocony[dlugosc_tablicy-i-1]
        i-=1


    j = 0
    nowy_wynik = [0] * (w*k)
    for i in range(w*k):
        if i % dlugosc_tablicy == 0:
            j = 0
        else:
            j+=1
        nowy_wynik[i] = wynik[j]

    x = nowy_wynik[(w*k)-1]
    return x

print(algorytm(4, 5, 179))