def odbicie(n: str) -> int:
    a = ""
    i = len(n) - 1

    while i >= 0:
        a += n[i]
        i -= 1

    return int(a)

def liczba_pierwsza(n: int) -> bool:
    i = 2

    if n == 0 or n == 1:
        return False

    while (i*i)<n:
        if n % i == 0:
            return False
        i+=1

    return True

with open("materialy/liczby.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

    for line in lines:
        if liczba_pierwsza(int(line)) and liczba_pierwsza(odbicie(line)):
            print(line)