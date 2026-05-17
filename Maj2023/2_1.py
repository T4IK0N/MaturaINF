n = int(input("podaj n: ")) #liczba dziesietna
if n == 0:
    exit()

binarnie = []
while n != 0:
    reszta = n % 2
    binarnie.append(str(reszta))
    n = n // 2

binarnie = binarnie[::-1]
print("".join(binarnie))

b = 1
for i in range(1, len(binarnie)):
    if binarnie[i] != binarnie[i - 1]:
        b += 1

print(b)