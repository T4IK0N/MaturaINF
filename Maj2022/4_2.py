def rozklad_na_czynniki_pierwsze(n):
    czynnik = 2 #w 1 by sie zblokowal w infinite loopce
    lista_czynnikow = []
    n = int(n)
    while n>1 and n%2==0:
        lista_czynnikow.append(czynnik)
        n/=czynnik

    czynnik+=1

    while n>1:
        if n % czynnik == 0:
            n = n / czynnik
            lista_czynnikow.append(czynnik)
        else:
            czynnik+=2
    return lista_czynnikow


def rozklad_na_czynniki_pierwsze_rozne(n):
    lista_czynnikow = rozklad_na_czynniki_pierwsze(n)
    if len(lista_czynnikow) == 0:
        return []

    czynniki_rozne = []
    for czynnik in lista_czynnikow:
        if czynnik not in czynniki_rozne:
            czynniki_rozne.append(czynnik)

    return czynniki_rozne

with open("d:\\programowanie\\inf_matura\\Maj2022\\materialy\\liczby.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    najwiecej_ilosc = 0
    najwiecej_liczba = []

    najwiecej_roznych_lista = []
    najwiecej_roznych_ilosc = 0
    najwiecej_roznych_liczba = []
    for i in range(len(lines)):
        aktualna_ilosc = len(rozklad_na_czynniki_pierwsze(lines[i]))
        aktualna_roznych_ilosc = len(rozklad_na_czynniki_pierwsze_rozne(lines[i]))

        if aktualna_ilosc > najwiecej_ilosc:
            najwiecej_ilosc = aktualna_ilosc
            najwiecej_liczba.append(lines[i])

        if aktualna_roznych_ilosc >= najwiecej_roznych_ilosc:
            najwiecej_roznych_ilosc = aktualna_roznych_ilosc
            najwiecej_roznych_liczba.append(lines[i])


    print(najwiecej_ilosc, ", ".join(najwiecej_liczba), "\n", najwiecej_roznych_ilosc, ", ".join(najwiecej_roznych_liczba))