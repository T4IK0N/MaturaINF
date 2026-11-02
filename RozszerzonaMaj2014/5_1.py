def is_prime(n):
    if n < 2:
        return False

    i = 2
    while i*i<=n:
        if n%i == 0:
            return False
        i+=1
    return True

with open("materialy/NAPIS.TXT") as f:
    lines = [line.strip() for line in f.readlines()]

    ilosc = 0
    for line in lines:
        suma = 0
        for letter in line:
            suma+=ord(letter)
        if is_prime(suma):
            ilosc+=1
    print(ilosc)