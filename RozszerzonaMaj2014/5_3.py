with open("materialy/NAPIS.TXT") as f:
    lines = [line.strip() for line in f.readlines()]

    powtarzajace_sie = []
    for i in range(len(lines)):
        for j in range(len(lines)):
            if lines[i] == lines[j] and i != j:
                powtarzajace_sie.append(lines[i])

    print("\n".join(set(powtarzajace_sie)))