def odbicie(n: str) -> int:
    a = ""
    i = len(n) - 1

    while i >= 0:
        a += n[i]
        i -= 1

    return int(a)

with open("materialy/liczby.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

    for line in lines:
        if odbicie(line) % 17 == 0:
            print(odbicie(line))