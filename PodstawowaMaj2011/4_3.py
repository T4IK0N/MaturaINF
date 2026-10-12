with open("materialy/hasla.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

    for line in lines:
        for i in range(len(line)-1):
            if ord(line[i]) + ord(line[i+1]) == 220:
                print(line)
                continue