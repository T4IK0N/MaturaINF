with open("materialy/pary.txt") as f:
    najlepsza = None

    for line in f:
        n, word = line.strip().split()

        if int(n) == len(word):
            para = (int(n), word)

            if najlepsza is None or para < najlepsza:
                najlepsza = para

    print(najlepsza[0], najlepsza[1])