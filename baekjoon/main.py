import sys


A = int(sys.stdin.readline().rstrip())
B = int(sys.stdin.readline().rstrip())
C = int(sys.stdin.readline().rstrip())


l = [0 for _ in range(10)]

for c in str(A * B * C):
    l[int(c)] += 1

for c in l:
    print(c)