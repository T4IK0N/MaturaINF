def xor(a, b): #a, b -> liczba binarnie
    wynik = []
    for i in range(len(a)):
        if a[i] != b[i]:
            wynik.append("1")
        else:
            wynik.append("0")
    return wynik

def przesun_binarnie(a):
    a = a.zfill(1+len(a))
    a = list(a)
    a.pop()
    return a

with open("bin.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

    with open("wyniki2_5.txt", "w") as p:
        for i in range(len(lines)):
            if i != 0:
                p.write('\n')
            p.write("".join(xor(lines[i], przesun_binarnie(lines[i]))))