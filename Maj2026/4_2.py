n = 50000

podwladni = [0] * (n + 1)

plik = open("materialy/korpo.txt", "r")

for i in range(1, n + 1):
    szef = int(plik.readline())
    if szef != 0:
        podwladni[szef] += 1

plik.close()

wynik = 0

for i in range(1, n + 1):
    if podwladni[i] == 0:
        wynik += 1

print(wynik)