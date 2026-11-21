def symuluj_runde(odbiorcy, pakiety):
    n = len(pakiety)
    nowe_pakiety = [[] for _ in range(n)]

    for komp in range(n):
        odb = odbiorcy[komp] - 1  # zamiana numeru 1..n na indeks 0..n-1
        for pakiet in pakiety[komp]:
            nowe_pakiety[odb].append(pakiet)

    return nowe_pakiety


with open("materialy/odbiorcy.txt", "r") as f:
    odbiorcy = [int(linia.strip()) for linia in f if linia.strip()]

n = len(odbiorcy)
pakiety = [[i + 1] for i in range(n)]

wyniki = []
for runda in range(1, 9):
    pakiety = symuluj_runde(odbiorcy, pakiety)
    if runda in (1, 2, 4, 8):
        najwiecej = max(len(x) for x in pakiety)
        wyniki.append(str(najwiecej))

print(" ".join(wyniki))