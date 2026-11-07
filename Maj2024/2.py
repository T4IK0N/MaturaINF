# n -> argument, n>0 z zalozenia
# c -> wynik

def funkcja(n):
    b = 1 #mnoznik
    c = 0
    ilosc=0
    while n>0:
        a = n % 10 #cyfra jednosci
        n = n//10 #liczba n zmniejszona o cyfre jednosci (zmniejszona o a)
        if a%2 == 0: #jesli a jest podzielne przez 2
            c = c + b * (a // 2) #suma c z b * dzielenie całkowite cyfry jedności przez 2 (9//2 to 4)
        else:
            ilosc+=1
            c = c + b #jesli cyfra jednosci nie jest podzielna, c + b
        b = b * 10 #b to mnoznik, powoduje ze zapisujemy liczbe od konca do znakow dziesiatek, setek itd.

    print(ilosc)
    return c

print("2.1")
print(funkcja(336058))
print(funkcja(542102))
print(funkcja(87654321012345678))

print("2.2")
print(funkcja(333333666666999999))