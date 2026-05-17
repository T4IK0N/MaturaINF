with open("pi.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    najdluzszy_ciag = []
    index_najdluzszego_ciagu = 0
    dlugosc_najdluzszego = 1

    n = len(lines)
    for i in range(len(lines)-3): #sprawdzamy od 1 do n-3 poniewaz minimalna dlugosc ciagu to 4
        aktualna_dlugosc = 1
        aktualny_ciag = [lines[i]]
        j = i
        if j > len(lines)-5: break #na chama ale dziala, jesli j bedzie mniejsze od konca-5 to przerwij

        #rosnacy (nie mogą być takie same więc <)
        while lines[j] < lines[j+1]:
            aktualna_dlugosc+=1
            aktualny_ciag.append(lines[j+1])
            j+=1

        #flaga ktora zabezpiecza ze jesli jest przemienny przestanie sprawdzac
        if lines[j] > lines[j+1] < lines[j+2]:
            aktualna_dlugosc += 1
            aktualny_ciag.append(lines[j+1])
            if aktualna_dlugosc > dlugosc_najdluzszego:
                dlugosc_najdluzszego = aktualna_dlugosc
                najdluzszy_ciag = aktualny_ciag
                index_najdluzszego_ciagu = i+1

            # print("PRZERYWAM W 1:", dlugosc_najdluzszego, aktualna_dlugosc, aktualny_ciag, "INDEX_K", index_k)
            continue

        # flaga która sprawdza czy element po k jest rowny, jesli jest okej i idź dalej (czyli ciąg może być 123 99 321)
        if lines[j] == lines[j+1]:
            aktualna_dlugosc+=1
            aktualny_ciag.append(lines[j+1])
            j+=1

        #malejacy (jest flaga ktora sprawdza czy jest rowny wiec mozna sprawdzac tylko mniejsze)
        while lines[j] > lines[j+1]:
            aktualna_dlugosc+=1
            aktualny_ciag.append(lines[j+1])
            j+=1

        if lines[j] < lines[j+1]:
            if aktualna_dlugosc > dlugosc_najdluzszego:
                dlugosc_najdluzszego = aktualna_dlugosc
                najdluzszy_ciag = aktualny_ciag
                index_najdluzszego_ciagu = i+1

            # print("PRZERYWAM W 2:", dlugosc_najdluzszego, aktualna_dlugosc, aktualny_ciag, "INDEX_K", index_k)
            continue

    print(index_najdluzszego_ciagu, "\n"+"".join(najdluzszy_ciag))