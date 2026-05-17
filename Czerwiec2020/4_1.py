import math

n = 101
A = []
for i in range(n):
    A.append(True)
A[0] = False
A[1] = False

def is_prime(liczba: int):
    for i in range(1, int(math.sqrt(n))):
        if A[i]:
            for j in range(i*i, n, i):
                A[j] = False


    return A[liczba]

with open("materialy\\pary.txt") as f:
    lines = [line.strip() for line in f.readlines()]
    n = len(lines)

    for i in range(n):
        pierwotna_liczba = int(lines[i][:lines[i].find(" ")])
        if pierwotna_liczba % 2 != 0:
            continue
        pierwsza_liczba = pierwotna_liczba
        druga_liczba = 0

        a = True

        while a:
            while not is_prime(pierwsza_liczba):
                pierwsza_liczba -= 1

            druga_liczba = pierwotna_liczba - pierwsza_liczba
            if pierwsza_liczba + druga_liczba == pierwotna_liczba and is_prime(druga_liczba):
                a = False
            else:
                pierwsza_liczba -= 1

        if pierwsza_liczba > druga_liczba:
            temp = pierwsza_liczba
            pierwsza_liczba = druga_liczba
            druga_liczba = temp

        print(f"{pierwotna_liczba} {pierwsza_liczba} {druga_liczba}")