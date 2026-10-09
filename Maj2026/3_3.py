plik = open("materialy/pary.txt", "r")

for linia in plik:
    s1, s2 = linia.split()

    maksimum = min(len(s1), len(s2))
    najdluzszy = 0

    for k in range(maksimum, 4, -1):

        if s1[:k] == s2[len(s2) - k:]:
            najdluzszy = k
            break

        if s2[:k] == s1[len(s1) - k:]:
            najdluzszy = k
            break

    if najdluzszy >= 5:
        print(s1 + " " + s2 + " " + str(najdluzszy))

plik.close()