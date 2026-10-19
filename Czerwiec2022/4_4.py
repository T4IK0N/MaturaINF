
with open("materialy/liczby.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

ilosc_roznych = 0
ilosc_powtorzonych_dwa_razy = 0
ilosc_powtorzonych_trzy_razy = 0

for i in range(len(lines)):
    liczba_sprawdzana = lines[i]

    if liczba_sprawdzana in lines[:i]:
        continue

    j = i+1
    ilosc_powtorzen = 0
    for j in range(len(lines)):
        if liczba_sprawdzana == lines[j]:
            ilosc_powtorzen+=1
    # mozna tez uzyc .count do zliczenia wystapien:
    # ilosc_powtorzen = lines.count(liczba_sprawdzana)

    ilosc_roznych += 1

    if ilosc_powtorzen == 2:
        ilosc_powtorzonych_dwa_razy += 1

    elif ilosc_powtorzen == 3:
        ilosc_powtorzonych_trzy_razy += 1

print("różne:", ilosc_roznych)
print("powtórzone dwa razy:", ilosc_powtorzonych_dwa_razy)
print("powtórzone trzy razy:", ilosc_powtorzonych_trzy_razy)
