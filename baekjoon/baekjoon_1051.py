# 숫자 정사각형
"""
N×M크기의 직사각형이 있다. 각 칸에는 한 자리 숫자가 적혀 있다.
이 직사각형에서 꼭짓점에 쓰여 있는 수가 모두 같은 가장 큰 정사각형을 찾는 프로그램을 작성하시오.
이때, 정사각형은 행 또는 열에 평행해야 한다.
"""
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
rectangle = []
max_square_size = min(N, M)

for _ in range(N):
    line = list(map(int, list(sys.stdin.readline().rstrip())))
    rectangle.append(line)

result = 1
for square_size in range(1, max_square_size):
    for i in range(N - square_size):
        for j in range(M - square_size):
            if rectangle[i][j] == rectangle[i][j+square_size] == rectangle[i+square_size][j] == rectangle[i+square_size][j+square_size]:
                result = (square_size + 1) ** 2
print(result)

