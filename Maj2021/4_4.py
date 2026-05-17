import string

with open("materialy\\instrukcje.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    n = len(lines)
    wynik = []

    for i in range(n):
        komenda = lines[i][:(lines[i].rfind(" "))] #np. DOPISZ, USUN
        reszta = lines[i][(lines[i].rfind(" "))+1] #np. 1, X
        if komenda == "DOPISZ":
            wynik.append(reszta)
        if komenda == "ZMIEN":
            wynik[-1] = reszta
        if komenda == "USUN":
            wynik.pop()
        if komenda == "PRZESUN":
            alfabet = string.ascii_uppercase
            for index, value in enumerate(wynik):
                if value == reszta:
                    if reszta == "Z":
                        wynik[index] = "A"
                    else:
                        wynik[index] = alfabet[alfabet.find(wynik[index]) + 1]
                    break

    print("".join(wynik))