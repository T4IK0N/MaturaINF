def odbicie(n: str) -> int:
    a = ""
    i = len(n) - 1

    while i >= 0:
        a += n[i]
        i -= 1

    return int(a)

with open("materialy/liczby.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    najwieksza_liczba = 0
    najwieksza_roznica = 0

    for line in lines:
        n = abs(int(line) - odbicie(line))
        if n:
            if n > najwieksza_roznica:
                najwieksza_liczba = line
                najwieksza_roznica = n
    print(najwieksza_liczba, najwieksza_roznica)