with open("d:\\programowanie\\inf_matura\\Czerwiec2024\\materialy\\slowa.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    ilosc = 0

    for index, value in enumerate(lines):
        for j in range(len(value)-2):
            if value[j] == "k" and value[j+2] == "t":
                ilosc += 1
    print(ilosc)