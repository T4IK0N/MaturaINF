with open("materialy/dane.txt", "r") as f:
    lines = "".join(f.readlines())

    ilosc=0
    for i in range(len(lines)-3):
        if i % 2 == 0: #nieparzyste gdyby liczyć od 1, parzyste gdy liczone od 0
            if lines[i] == lines[i+2] and lines[i+1] == lines[i+3]:
                ilosc+=1
    print(ilosc)