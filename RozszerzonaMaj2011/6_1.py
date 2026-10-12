with open("materialy/liczby.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    parzyste = 0
    for line in lines:
        if line[-1] == "0":
            parzyste+=1
    print(parzyste)