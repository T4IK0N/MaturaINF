with open("materialy/liczby.txt") as f:
    lines = [line.strip() for line in f.readlines()][0].split()
    lines = [int(line) for line in lines]

    # 1 sposób (działa, ale trwa wieki, liczy sume od zera przy każdej iteracji)
    najwieksza_srednia = 0
    dla_ilu = 0
    zaczyna_sie = 0
    for k in range(50, len(lines)+1):
        i=0
        while i < len(lines)-k:
            ilosc_liczb = k
            suma = 0
            for j in range(i, ilosc_liczb+i):
                suma += lines[j]
            srednia = suma / ilosc_liczb
            if srednia > najwieksza_srednia:
                najwieksza_srednia = srednia
                dla_ilu = ilosc_liczb
                zaczyna_sie = lines[i]
            # print(srednia, ilosc_liczb)
            i+=1
    print(najwieksza_srednia, dla_ilu, zaczyna_sie)

    # 2 sposób, sumy prefiksowe (clean rozwiązanie)
    prefiks = [0]
    for line in lines:
        prefiks.append(prefiks[-1] + line)
    najwieksza_srednia = 0
    najwieksza_suma = 0
    dla_ilu = 0
    zaczyna_sie = 0
    for k in range(50, len(lines) + 1):
        i = 0
        while i + k <= len(lines):
            suma = prefiks[i + k] - prefiks[i]
            srednia = suma / k
            if srednia > najwieksza_srednia or dla_ilu == 0:
                najwieksza_suma = suma
                najwieksza_srednia = suma / k
                dla_ilu = k
                zaczyna_sie = lines[i]
            i += 1
    print(najwieksza_srednia, dla_ilu, zaczyna_sie)