with open("materialy/hasla.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

    parzyste=0
    nieparzyste=0
    for line in lines:
        if len(line) % 2 == 0:
            parzyste+=1
        else:
            nieparzyste+=1

    print("parzyste:", parzyste, "nieparzyste:", nieparzyste)