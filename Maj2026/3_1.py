plik = open("materialy/pary.txt", "r")

najwieksza = -1
naj_s1 = ""
naj_s2 = ""

for linia in plik:
    s1, s2 = linia.split()

    suma1 = 0
    suma2 = 0

    for znak in s1:
        suma1 += ord(znak)

    for znak in s2:
        suma2 += ord(znak)

    roznica = abs(suma1 - suma2)

    if roznica > najwieksza:
        najwieksza = roznica
        naj_s1 = s1
        naj_s2 = s2

plik.close()
print(naj_s1 + " " + naj_s2 + " " + str(najwieksza))