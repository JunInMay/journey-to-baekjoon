# 정수 삼각형
"""
위 그림은 크기가 5인 정수 삼각형의 한 모습이다.

맨 위층 7부터 시작해서 아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때,
이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성하라.
아래층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있다.

삼각형의 크기는 1 이상 500 이하이다.
삼각형을 이루고 있는 각 수는 모두 정수이며, 범위는 0 이상 9999 이하이다.
"""
import sys

N = int(sys.stdin.readline().rstrip())
triangle = []
maxes = []
for i in range(N):
    line = list(map(int, sys.stdin.readline().rstrip().split()))
    maxes.append([0 for _ in range(len(line))])
    triangle.append(line)

maxes[0][0] = triangle[0][0]

for i in range(1, N):
    for j in range(len(maxes[i])):
        if j == 0:
            maxes[i][j] = maxes[i-1][j] + triangle[i][j]
        elif j == len(maxes[i])-1:
            maxes[i][j] = maxes[i-1][j-1] + triangle[i][j]
        else:
            maxes[i][j] = max(maxes[i-1][j-1], maxes[i-1][j]) + triangle[i][j]

print(max(maxes[N-1]))