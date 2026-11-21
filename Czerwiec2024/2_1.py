ilosc = 0
def funkcja(x):
    global ilosc
    ilosc+=1
    if x == 0:
        return 0
    else:
        return 2 + funkcja(x//2)

print(funkcja(511), ilosc)