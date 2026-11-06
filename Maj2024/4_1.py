with open("materialy/liczby.txt") as f:
    lines = [line.strip() for line in f.readlines()]
    lines1 = lines[0].split()
    lines2 = lines[1].split()


    ilosc = 0
    for line1 in lines1:
        for line2 in lines2:
            if int(line2) % int(line1) == 0:
                ilosc+=1
                break
    print(ilosc)