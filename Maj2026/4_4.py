n = 50000
szef = [0] * (n + 1)
liczba_przelozonych = [0] * (n + 1)
plik = open("materialy/korpo.txt", "r")

for i in range(1, n + 1):
    szef[i] = int(plik.readline())
plik.close()

for i in range(2, n + 1):
    liczba_przelozonych[i] = liczba_przelozonych[szef[i]] + 1
najwiecej = 0

for i in range(1, n + 1):
    if liczba_przelozonych[i] > najwiecej:
        najwiecej = liczba_przelozonych[i]
ile = 0

for i in range(1, n + 1):
    if liczba_przelozonych[i] == najwiecej:
        ile += 1
print(najwiecej, ile)