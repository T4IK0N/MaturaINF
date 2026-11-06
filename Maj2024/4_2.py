with open("materialy/liczby.txt") as f:
    lines = [line.strip() for line in f.readlines()][0].split()

    # 1 sposób
    for i in range(len(lines)):
        for j in range(len(lines)):
            if int(lines[i]) > int(lines[j]):
                temp = int(lines[i])
                lines[i] = int(lines[j])
                lines[j] = temp
    print(lines[102])

    # 2 sposób (typowy python użytkownik)
    lines = [int(line) for line in lines]
    lines.sort(reverse=True)
    print(lines[102])