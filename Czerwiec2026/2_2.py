# funkcja
"""
def algorytm(n, T):
    k = n-1
    while k > 0:
        czy_podobne = True
        j = 0
        while j < k:
            if T[j] != T[n-k+j]:
                czy_podobne = False
            if czy_podobne:
                return k
            j+=1
        k-=1
    return 0

print(algorytm(10, [1,2,3,4]))
"""

# algorytm
while k > 0:
    czy_podobne = True
    j = 0
    while j < k:
        if T[j] != T[n-k+j]:
            czy_podobne = False
        j+=1
    if czy_podobne:
        break
    k-=1