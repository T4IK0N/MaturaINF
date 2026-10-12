with open("materialy/dane.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    ilosc = 0

    for line in lines:
        if line[0] == line[-1]:
            ilosc+=1
    print(ilosc)