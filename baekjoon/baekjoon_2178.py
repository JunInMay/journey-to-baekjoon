# 미로 탐색
"""
N×M크기의 배열로 표현되는 미로가 있다.

1	0	1	1	1	1
1	0	1	0	1	0
1	0	1	0	1	1
1	1	1	0	1	1
미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다.
이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오.
한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.
"""
import sys
from collections import deque

H, W = map(int, sys.stdin.readline().rstrip().split())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

graph = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(H)]

def bfs(start):
    queue = deque([start])
    while queue:
        node = queue.popleft()
        y, x = node
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < W and 0 <= ny < H and graph[ny][nx] == 1:
                graph[ny][nx] += graph[y][x]
                queue.append((ny, nx))

bfs((0,0))
print(graph[H-1][W-1])