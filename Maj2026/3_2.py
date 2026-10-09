plik = open("materialy/pary.txt", "r")

najwieksza = -1
naj_s1 = ""
naj_s2 = ""

for linia in plik:
    s1, s2 = linia.split()

    suma = 0

    for kod in range(ord('a'), ord('z') + 1):
        litera = chr(kod)

        liczba1 = s1.count(litera)
        liczba2 = s2.count(litera)

        if liczba1 < liczba2:
            suma += liczba1
        else:
            suma += liczba2

    if suma > najwieksza:
        najwieksza = suma
        naj_s1 = s1
        naj_s2 = s2

plik.close()
print(naj_s1 + " " + naj_s2 + " " + str(najwieksza))