# def funkcja(n, m, A):
#     P = []
#     for i in range(n):
#         T = []
#         for j in range(m):
#             T.append(True)
#         P.append(T)
#
#     for i in range(0, n):
#         for j in range(0, m):
#             if A[i][j] == 0:
#                 P[i][j] = False
#             else:
#                 if i == 0 and j != 0:
#                     P[i][j] = P[i][j-1]
#                 if i != 0 and j == 0:
#                     P[i][j] = P[i-1][j]
#                 if i != 1 and j != 1:
#                     P[i][j] = P[i][j-1] or P[i-1][j]
#     print(P)
#     return P[n-1][m-1]
#
# # B = [[1,1,1], [0,1,0], [1,1,1]]
# # print(funkcja(3, 3, B))
#
# # B = [[1,1,1], [0,0,1], [1,1,1], [1,0,0], [1,1,1]]
# # print(funkcja(5,3,B))
#
# # B = [[1,0,0,0,0], [1,1,0,0,1], [0,1,0,0,1], [0,1,1,1,0], [0,1,0,1,1]]
# # print(funkcja(5,5,B))


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
    print(P)
    return P[n-1][m-1]

# w pierwszym wierszu zawsze bedzie to co w pierwszej kolumnie chyba że była czarna to wtedy be

print(funkcja(3,3,[[1,1,1],[0,1,0],[1,1,1]]))
print(funkcja(5,3,[[1,1,1],[0,0,1],[1,1,1],[1,0,0],[1,1,1]]))
print(funkcja(5,5,[[1,0,0,0,0],[1,1,0,0,1],[0,1,0,0,1],[0,1,1,1,0],[0,1,0,1,1]]))