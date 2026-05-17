with open("pi.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    ilosc = 0

    for i in range(1, len(lines)): #iterujemy od 1 bo bede sprawdzac od tylu, od -1 do 0
        wartosc_dwucyfrowa = lines[i-1] + lines[i]
        if wartosc_dwucyfrowa > "90":
            ilosc+=1
    print(ilosc)