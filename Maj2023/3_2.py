with open("pi.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]
    min_fragment = ""
    min_ilosc = -1
    max_fragment = ""
    max_ilosc = -1

    for num in range(0, 100):
        aktualny_fragment = f"{num:02d}"
        aktualny_ilosc = 0

        for i in range(1, len(lines)): #iterujemy od 1 bo bede sprawdzac od tylu, od -1 do 0
            if aktualny_fragment == lines[i - 1] + lines[i]:
                aktualny_ilosc += 1

        if aktualny_ilosc > max_ilosc or max_ilosc == -1:
            max_ilosc = aktualny_ilosc
            max_fragment = aktualny_fragment

        if aktualny_ilosc < min_ilosc or min_ilosc == -1:
            min_ilosc = aktualny_ilosc
            min_fragment = aktualny_fragment

    print(min_fragment, min_ilosc, max_fragment, max_ilosc)