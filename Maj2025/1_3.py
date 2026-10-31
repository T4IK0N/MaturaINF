def p(n):
    r = n%100
    a = r//10
    b = r%10
    n = n//100

    if n > 0:
        w = a + (10*b) + 100 * p(n)
    else:
        if a > 0:
            w = a + (10*b)
        else:
            w = b
    return w

print(p(18293756182375687123567))

def p_iter(n):
    w = 0
    mult = 1

    while True:
        r = n % 100
        a = r // 10
        b = r % 10
        n = n // 100

        if n > 0:
            w = w + (a + 10 * b) * mult
            mult *= 100
        else:
            if a > 0:
                w = w + (a + 10 * b) * mult
            else:
                w = w + b * mult
            break

    return w

print(p_iter(18293756182375687123567))