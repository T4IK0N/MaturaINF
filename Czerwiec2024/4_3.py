def symuluj_runde(instrukcja: dict, lista_poprzednia: list):
    lista_nowa = [0] * len(lista_poprzednia)
    for komputer in range(1, len(lista_poprzednia) + 1):
        odbiorca = instrukcja[komputer]
        for pakiet in lista_poprzednia[komputer - 1]:
            lista_nowa[odbiorca - 1].append(pakiet)
    return lista_nowa


with open("d:\\programowanie\\inf_matura\\Czerwiec2024\\materialy\\odbiorcy_przyklad_moj.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

    n = len(lines)

    instrukcja = {}
    for i in range(n):
        instrukcja[i + 1] = int(lines[i])

    aktualna_lista = [[] for _ in range(n)]
    for i in range(n):
        aktualna_lista[i].append(i + 1)

    numer_rundy = 1
    znaleziono = False

    while not znaleziono:
        nowa_lista = [[] for _ in range(n)]

        for komputer in range(1, n + 1):
            odbiorca = instrukcja[komputer]
            for pakiet in aktualna_lista[komputer - 1]:
                nowa_lista[odbiorca - 1].append(pakiet)

        for komputer in range(1, n + 1):
            if komputer in nowa_lista[komputer - 1]:
                znaleziono = True
                print(f"{numer_rundy} {komputer}")
                break

        aktualna_lista = nowa_lista
        numer_rundy += 1