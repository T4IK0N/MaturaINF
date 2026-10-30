with open("materialy/symbole.txt") as f:
    lines_old = [line.strip() for line in f.readlines()]
    lines = []

    for i in range(len(lines_old)):
        lines_temp = ""
        for j in range(len(lines_old[i])):
            if lines_old[i][j]=='o':
                lines_temp+="0"
            if lines_old[i][j]=='+':
                lines_temp+="1"
            if lines_old[i][j]=='*':
                lines_temp+="2"
        lines.append(lines_temp)

    najwieksza = 0
    najwieksza_symbole = ""
    for i in range(len(lines)):
        if int(lines[i], 3) > najwieksza:
            najwieksza = int(lines[i], 3)
            najwieksza_symbole = lines_old[i]
    print(najwieksza, najwieksza_symbole)