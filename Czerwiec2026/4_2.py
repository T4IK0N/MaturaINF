with open("materialy/mapa.txt", "r") as f:
    lines = [line.split() for line in f.readlines()]

    najmniejsza_odleglosc = 1928571928387
    pary_najmniejszych_miast = []
    for i in range(len(lines)):
        for j in range(len(lines)):
            if i == j: continue
            x1, x2 = int(lines[i][0]), int(lines[j][0])
            y1, y2 = int(lines[i][1]), int(lines[j][1])
            d = abs(x1 - x2) + abs(y1 - y2)

            if d < najmniejsza_odleglosc:
                najmniejsza_odleglosc = d

    for i in range(len(lines)):
        for j in range(len(lines)):
            x1, x2 = int(lines[i][0]), int(lines[j][0])
            y1, y2 = int(lines[i][1]), int(lines[j][1])
            d = abs(x1 - x2) + abs(y1 - y2)
            miasto1, miasto2 = i+1, j+1
            if j+1 < i+1: #pomijamy zdublowane
                continue

            if d == najmniejsza_odleglosc:
                pary_najmniejszych_miast.append([miasto1, miasto2])
    print(najmniejsza_odleglosc)
    for para in pary_najmniejszych_miast:
        print(para)