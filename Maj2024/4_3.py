with open("materialy/liczby.txt") as f:
    lines = [line.strip() for line in f.readlines()]
    lines1 = [int(line) for line in lines[0].split()]
    lines2 = [int(line) for line in lines[1].split()]

    for line2 in lines2:
        old_line2 = line2
        czynniki = []
        for line1 in lines1:
            if line2 % line1 == 0: #jest dzielnikiem
                line2 //= line1
                czynniki.append(line1)

        wynik = 1
        for czynnik in czynniki:
            wynik*=czynnik
        if wynik == old_line2:
            print(old_line2)