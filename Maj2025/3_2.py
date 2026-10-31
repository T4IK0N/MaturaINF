with open("materialy/dron.txt") as f:
    lines = [line.strip() for line in f.readlines()]

    pkt_x, pkt_y, ilosc = 0, 0, 0
    for i in range(len(lines)):
        x, y = lines[i].split()
        pkt_x = pkt_x + int(x)
        pkt_y = pkt_y + int(y)

        if 0 < pkt_x < 5000 and 0 < pkt_y < 5000:
            ilosc+=1
    print("a)", ilosc)

    x1, y1 = 0, 0
    znaleziono = False
    for i in range(len(lines)):
        lines_x1, lines_y1 = lines[i].split()
        x1 = x1 + int(lines_x1)
        y1 = y1 + int(lines_y1)

        x2, y2 = 0, 0
        if znaleziono: break
        for j in range(len(lines)):
            lines_x2, lines_y2 = lines[j].split()
            x2 = x2 + int(lines_x2)
            y2 = y2 + int(lines_y2)

            x3, y3 = 0, 0
            if znaleziono: break
            for k in range(len(lines)):
                lines_x3, lines_y3 = lines[k].split()
                x3 = x3 + int(lines_x3)
                y3 = y3 + int(lines_y3)

                if (x1+x2)/2 == x3 and (y1+y2)/2 == y3 and x1 != x2 != x3 and y1 != y2 != y3:
                    print("b)", x1, y1, x2, y2, x3, y3)
                    znaleziono = True
                    break