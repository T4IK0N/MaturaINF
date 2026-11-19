# 1 sposób
def funkcja1(w: int, k: int, n: int) -> int:
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


    i = 0
    j = 0
    nowy_wynik = [0] * (w*k)
    while i < w*k:
        if i % dlugosc_tablicy == 0:
            j = 0
        else:
            j+=1
        nowy_wynik[i] = wynik[j]
        i+=1

    x = nowy_wynik[(w*k)-1]
    return x

print(algorytm(4, 5, 179))

# 2 sposób
def na_binarny(x):
    x2 = x
    dlugosc_tablicy = 0
    while x != 0:
        x //= 2
        dlugosc_tablicy+=1

    tablica_odwrocona = [0] * dlugosc_tablicy
    x = x2
    i = 0
    while i<dlugosc_tablicy:
        tablica_odwrocona[i] = x % 2
        x //= 2
        i+=1

    tablica = [0] * dlugosc_tablicy
    i = 0
    while i < dlugosc_tablicy:
        tablica[i] = tablica_odwrocona[dlugosc_tablicy-1-i]
        i+=1

    return tablica

def dlugosc_n_binarnie(x):
    dlugosc_tablicy = 0
    while x != 0:
        x //= 2
        dlugosc_tablicy += 1
    return dlugosc_tablicy

def funkcja2(w, k, n):
    tablica = [0] * (w*k)
    n_binarnie = na_binarny(n)
    len_n_binarnie = dlugosc_n_binarnie(n)

    i = 0
    while i < w*k:
        tablica[i] = n_binarnie[i%len_n_binarnie]
        i+=1
    return tablica[(w*k)-1]

print(funkcja(4, 5, 179))