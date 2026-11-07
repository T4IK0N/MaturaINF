def funkcja(n, m, A):
    P = [[False for _ in range(m)] for _ in range(n)]
    P[0][0] = True
    for i in range(0, n):
        for j in range(0, m):
            if A[i][j] == 0:
                P[i][j] = False
            else:
                if i == 0 and j != 0:
                    P[i][j] = P[i][j-1]
                elif i != 0 and j == 0:
                    P[i][j] = P[i-1][j]
                elif i != 0 and j != 0:
                    P[i][j] = P[i][j-1] or P[i-1][j]
    # print(P)
    return P[n-1][m-1]

print("a)")
print(funkcja(5,5,[
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,1,1,0],
    [1,1,1,0,1]
]))
print("b)")
print(funkcja(4,4,[
    [1,0,0,0],
    [1,0,0,0],
    [1,0,0,0],
    [1,1,1,1]
]))