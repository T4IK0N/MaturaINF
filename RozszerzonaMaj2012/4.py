import string
szyfr = {}
for i in range(len(string.ascii_uppercase)):
    szyfr.update({string.ascii_uppercase[i]: i+1})

ascii_szyfr = {}
j=0
for i in range(65, 91):
    ascii_szyfr.update({i: string.ascii_uppercase[j]})
    j+=1

ascii_szyfr_litera = {}
j=0
for i in range(65, 91):
    ascii_szyfr_litera.update({string.ascii_uppercase[j]: i})
    j+=1

def szyfrowanie(tekst_jawny, klucz):
    szyfrogram = ""

    n = len(tekst_jawny)
    i=0
    j=0

    while i < n:
        if i >= len(klucz):
            i = 0
        suma = ascii_szyfr_litera[tekst_jawny[j]] + szyfr[klucz[i]]
        if suma > 90:
            suma-=26
        szyfrogram += ascii_szyfr[suma]
        i+=1
        j+=1

        if len(szyfrogram) == len(tekst_jawny):
            break
    return szyfrogram

def deszyfrowanie(szyfrogram, klucz):
    tekst_jawny = ""

    n = len(szyfrogram)
    i=0
    j=0

    while i < n:
        if i >= len(klucz):
            i = 0
        roznica = ascii_szyfr_litera[szyfrogram[j]] - szyfr[klucz[i]]
        if roznica < 65:
            roznica+=26
        tekst_jawny += ascii_szyfr[roznica]
        i+=1
        j+=1

        if len(tekst_jawny) == len(szyfrogram):
            break
    return tekst_jawny

with open("materialy/tj.txt", "r") as tj:
    with open("materialy/klucze1.txt", "r") as klucze:
        lines_tj = [line.strip() for line in tj.readlines()]
        lines_klucze = [line.strip() for line in klucze.readlines()]

        print("4a")
        for i in range(len(lines_tj)):
            print(szyfrowanie(lines_tj[i], lines_klucze[i]))

with open("materialy/sz.txt", "r") as sz:
    with open("materialy/klucze2.txt", "r") as klucze:
        lines_sz = [line.strip() for line in sz.readlines()]
        lines_klucze = [line.strip() for line in klucze.readlines()]

        print("4b")
        for i in range(len(lines_sz)):
            print(deszyfrowanie(lines_sz[i], lines_klucze[i]))