# RGB거리
"""
RGB거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.

집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다.
각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.

1번 집의 색은 2번 집의 색과 같지 않아야 한다.
N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.
"""
import sys
n = int(sys.stdin.readline().rstrip())

costs = []
for _ in range(n):
    costs.append(list(map(int, sys.stdin.readline().rstrip().split())))

min_costs = []

for i in range(len(costs)):
    if len(min_costs) == 0:
        min_costs.append(costs[i])
    else:
        R = min(min_costs[i-1][1], min_costs[i-1][2]) + costs[i][0]
        G = min(min_costs[i-1][0], min_costs[i-1][2]) + costs[i][1]
        B = min(min_costs[i-1][0], min_costs[i-1][1]) + costs[i][2]
        min_costs.append([R, G, B])

print(min(min_costs[-1]))