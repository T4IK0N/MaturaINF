with open("materialy/dane.txt", "r") as f:
    lines_osemkowo = [line.strip() for line in f.readlines()]
    lines_dziesietnie = []

    for osemkowo in lines_osemkowo:
        dziesietnie = 0
        n = len(osemkowo)
        for i in range(n):
            dziesietnie += int(osemkowo[i]) * (8 ** (n-i-1))
        lines_dziesietnie.append(str(dziesietnie))

    ile_liczb = 0
    for line in lines_dziesietnie:
        if line[0] == line[-1]:
            ile_liczb+=1
    print(ile_liczb)
