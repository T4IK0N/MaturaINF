def symuluj_runde(instrukcja: dict, lista_poprzednia: list):
    lista_nowa = [0] * len(lista_poprzednia)
    for komputer in range(1, len(lista_poprzednia) + 1):
        odbiorca = instrukcja[komputer]
        for pakiet in lista_poprzednia[komputer - 1]:
            lista_nowa[odbiorca - 1].append(pakiet)
    return lista_nowa

with open("materialy/odbiorcy_przyklad.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    print(lines)