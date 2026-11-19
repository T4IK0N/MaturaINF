with open("materialy/odbiorcy.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    ilosc = 0
    lista_wszystkich = []
    n = len(lines)

    for i in range(n):
        lista_wszystkich.append(int(lines[i]))
    for i in range(1, n+1):
        if i not in lista_wszystkich:
            ilosc+=1
    print(ilosc)