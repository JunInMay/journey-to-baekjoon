Lin = []
N, M = map(int, input().split())
for i in range(N):
    Lu = list(input().split(','))
    Lin.append(Lu)

for i in range(M):
    for j in range(i):
        Mx = {}
        for k in range(N):

            u = (Lin[k][i], Lin[k][j])
            print(f"i, j = {i}, {j}")
            print(u)
            if u in Mx:
                print("NO")
                print(f"{Mx[u] + 1} {k + 1}")
                print(f"{j+1} {i+1}")
                exit(0)
            Mx[u] = k
print("YES")

"""
12 10
A1,A2,A3,A4,A5,A6,A7,A8,A9,A10
B1,B2,B3,B4,B5,B6,B7,B8,B9,B10
C1,C2,C3,C4,C5,C6,C7,C8,C9,C10
D1,D2,D3,D4,D5,D6,D7,D8,D9,D10
E1,E2,E3,E4,E5,E6,E7,E8,E9,E10
Z1,Z2,Z3,Z4,Z5,Z6,Z7,Z8,Z9,Z10
Y1,Y2,Y3,Y4,Y5,Y6,Y7,Y8,Y9,Y10
X1,X2,X3,X4,X5,X6,X7,X8,X9,X10
W1,W2,W3,W4,W5,W6,W7,W8,W9,W10
V1,V2,V3,V4,V5,V6,V7,V8,V9,V10
H1,H2,H3,H4,H5,H6,H7,H8,H9,H10
G1,G2,G3,G4,G5,A6,A7,A8,A9,A10
"""