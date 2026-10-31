def nwd(a: int, b_parametr: int):
    if b_parametr == 0:
        return a

    if b_parametr < 0:
        b = b_parametr*(-1)
    else:
        b = b_parametr

    while a != b:
        if a>b:
            a-=b
        else:
            b-=a
    return a

with open("materialy/dron.txt") as f:
    lines = [line.strip() for line in f.readlines()]

    ilosc=0
    for line in lines:
        x, y = line.split()
        if nwd(int(x), int(y)) > 1:
            ilosc+=1
    print(ilosc)