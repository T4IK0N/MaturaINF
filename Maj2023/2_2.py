def licz_bloki(n):
    liczba_blokow = 1
    for i in range(1, len(n)):
        if n[i] != n[i - 1]:
            liczba_blokow += 1
    return liczba_blokow

with open("bin.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    ilosc_liczb = 0

    for i in range(len(lines)):
        liczba_blokow = licz_bloki(lines[i])
        if liczba_blokow <= 2: #zrobiles tutaj >= zamiast <= czytaj ZADANIA!
            ilosc_liczb += 1

print(ilosc_liczb)