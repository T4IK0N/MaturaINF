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

    suma = 0
    for i in range(len(lines)):
        suma += int(lines[i], 3)

    suma_trojkowo = ""
    suma_dziesietnie = suma
    while suma_dziesietnie > 0:
        if suma_dziesietnie % 3 == 0:
            suma_trojkowo += "o"
        elif suma_dziesietnie % 3 == 1:
            suma_trojkowo += "+"
        elif suma_dziesietnie % 3 == 2:
            suma_trojkowo += "*"
        suma_dziesietnie = suma_dziesietnie // 3

    print(suma, suma_trojkowo[::-1])
