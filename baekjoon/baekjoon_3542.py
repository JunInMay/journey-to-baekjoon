# Database
"""
Peter studies the theory of relational databases.
Table in the relational database consists of values that are arranged in rows and columns.

There are different normal forms that database may adhere to.
Normal forms are designed to minimize the redundancy of data in the database.
For example, a database table for a library might have a row for each book and columns for book name, book author, and author’s email.

If the same author wrote several books, then this representation is clearly redundant.
To formally define this kind of redundancy Peter has introduced his own normal form. A table is in Peter’s Normal Form (PNF) if and only if there is no pair of rows and a pair of columns such that the values in the corresponding columns are the same for both rows.

The above table is clearly not in PNF, since values for 2rd and 3rd columns repeat in 2nd and 3rd rows.
However, if we introduce unique author identifier and split this table into two tables
— one containing book name and author id, and the other containing book id, author name, and author email, then both resulting tables will be in PNF.
Given a table your task is to figure out whether it is in PNF or not.
"""
"""
문제를 잘못 이해해서 사실상 답보고, 이해한 뒤에 풂.
"""
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
table = []
for _ in range(N):
    table.append(sys.stdin.readline().rstrip().split(','))

result = "YES"
for i in range(M-1):
    for j in range(i+1, M):
        hash = {}
        for h in range(N):
            if (table[h][i], table[h][j]) in hash:
                result = "NO"
                print("NO")
                print(hash[(table[h][i], table[h][j])]+1, h+1)
                print(i+1, j+1)
                exit(0)
            hash[(table[h][i], table[h][j])] = h
print(result)

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