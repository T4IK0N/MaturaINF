def is_prime(n):
    if n == 0 or n == 1:
        return False

    i = 2
    while i*i<n:
        if n % i == 0:
            return False
        i+=1
    return True

with open("materialy/dane.txt", "r") as f:
    lines = "".join(f.readlines())

    najwieksza_suma = 0
    najwiekszy_ciag = ""
    for i in range(0, len(lines)-1, 2):
        sumy_prefiksowe = []
        ciag = []
        suma = 0
        for j in range(i, len(lines)-1, 2):
            suma += ord(lines[j]) + ord(lines[j+1])
            sumy_prefiksowe.append(suma)
            ciag.append(lines[j] + lines[j+1])

        for k in range(len(sumy_prefiksowe)):
            if sumy_prefiksowe[k] > najwieksza_suma and is_prime(sumy_prefiksowe[k]):
                najwieksza_suma = sumy_prefiksowe[k]
                najwiekszy_ciag = ""
                for x in range(0, k+1):
                    najwiekszy_ciag+=ciag[x]
    print(najwiekszy_ciag)

