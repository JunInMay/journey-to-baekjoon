# N-Queen
"""
N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.
"""
import sys
n = int(sys.stdin.readline().rstrip())
result = 0
left_diagonal = [False] * (n*2-1)
top_vertical = [False] * n
right_diagonal = [False] * (n*2-1)

def nQueen(floor):
    global n, result
    if floor == n:
        result += 1

    for i in range(n):
        if not(left_diagonal[i-floor+n-1] or top_vertical[i] or right_diagonal[i+floor]):
            left_diagonal[i - floor + n - 1] = top_vertical[i] = right_diagonal[i + floor] = True
            nQueen(floor+1)
            left_diagonal[i - floor + n - 1] = top_vertical[i] = right_diagonal[i + floor] = False

nQueen(0)
print(result)