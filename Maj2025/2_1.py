with open("materialy/symbole.txt") as f:
    lines = [line.strip() for line in f.readlines()]

    for line in lines:
        if line == line[::-1]:
            print(line)
