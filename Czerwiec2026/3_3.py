with open("materialy/dane.txt", "r") as f:
    lines = "".join(f.readlines())

    lines_pary = []
    for i in range(0, len(lines)-1, 2):
        para = lines[i] + lines[i+1]
        lines_pary.append(para)
    lines_distinct = list(set(lines_pary))

    lines_dict = {}
    for i in range(len(lines_distinct)):
        lines_dict.update({lines_distinct[i]: lines_pary.count(lines_distinct[i])})

    lines_dict_posortowany = dict(
        sorted(lines_dict.items(), key=lambda items : items[1])
    )
    print("".join(lines_dict_posortowany.keys()))