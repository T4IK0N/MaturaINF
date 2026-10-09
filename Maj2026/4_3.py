n = 50000

podwladni = [0] * (n + 1)

plik = open("materialy/korpo.txt", "r")

for i in range(1, n + 1):
    szef = int(plik.readline())
    if szef != 0:
        podwladni[szef] += 1

plik.close()

najwiecej = 0
pracownik = 0

for i in range(1, n + 1):
    if podwladni[i] > najwiecej:
        najwiecej = podwladni[i]
        pracownik = i

print(pracownik, najwiecej)