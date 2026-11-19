def szyfr(n, T, k):
    a = n // k
    c = n-a
    S = [0] * n
    for i in range(0, n):
        if i+1 % k == 0:
            b = i // k
            S[n-a+b] = T[i]
        else:
            S[c] = T[i]
            c -= 1
    return S
print("".join(szyfr(14, list("defragmentacja"), 3)))
print("".join(szyfr(10, list("tropikalny"), 11)))