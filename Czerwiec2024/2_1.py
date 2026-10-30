def funkcja(x):
    if x == 0:
        return 0
    else:
        return 2 + funkcja(x//2)

print(funkcja(511))

# for i in range(250)