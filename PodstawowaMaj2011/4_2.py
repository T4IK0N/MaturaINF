with open("materialy/hasla.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

    for line in lines:
        if line[::-1] == line:
            print(line)