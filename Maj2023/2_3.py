def binarnie_na_dziesietnie(n): #horner
    if n == 0:
        return 0

    wynik = int(n[0])
    for i in range(1, len(n)):
        wynik = (wynik * 2) + int(n[i])
    return wynik

with open("bin.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    liczba_dziesietnie = 0
    liczba_binarnie = []

    for i in range(len(lines)):
        aktualna_liczba_dziesietnie = binarnie_na_dziesietnie(lines[i])

        if aktualna_liczba_dziesietnie > liczba_dziesietnie:
            liczba_binarnie = lines[i]
            liczba_dziesietnie = aktualna_liczba_dziesietnie

print(liczba_binarnie)