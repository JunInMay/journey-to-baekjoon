# 구간 합 구하기 5
"""
N×N개의 수가 N×N 크기의 표에 채워져 있다. (x1, y1)부터 (x2, y2)까지 합을 구하는 프로그램을 작성하시오. (x, y)는 x행 y열을 의미한다.
예를 들어, N = 4이고, 표가 아래와 같이 채워져 있는 경우를 살펴보자.

1	2	3	4
2	3	4	5
3	4	5	6
4	5	6	7

여기서 (2, 2)부터 (3, 4)까지 합을 구하면 3+4+5+4+5+6 = 27이고, (4, 4)부터 (4, 4)까지 합을 구하면 7이다.
표에 채워져 있는 수와 합을 구하는 연산이 주어졌을 때, 이를 처리하는 프로그램을 작성하시오.
"""
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
array = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
sum_square_array = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(N):
    for j in range(N):
        sum_square_array[i+1][j+1] = sum_square_array[i][j+1] + sum_square_array[i+1][j] - sum_square_array[i][j] + array[i][j]

for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
    result = sum_square_array[x2][y2] - sum_square_array[x2][y1-1] - sum_square_array[x1-1][y2] + sum_square_array[x1-1][y1-1]
    print(result)