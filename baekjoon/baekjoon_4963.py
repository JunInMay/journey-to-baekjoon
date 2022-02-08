# 섬의 개수
"""
정사각형으로 이루어져 있는 섬과 바다 지도가 주어진다. 섬의 개수를 세는 프로그램을 작성하시오.
한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다.

두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다.
지도는 바다로 둘러싸여 있으며, 지도 밖으로 나갈 수 없다.
"""
import sys
from collections import deque

# 12시부터 시계방향으로
dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

def dfs(start):
    y, x = start
    stack = deque([(x, y)])
    visited[y][x] = True
    while stack:
        x, y = stack.pop()
        # 시계방향 탐색
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > (W-1) or ny < 0 or ny > (H-1):
                continue
            if not visited[ny][nx] and graph[ny][nx]:
                stack.append((nx, ny))
                visited[ny][nx] = True

W, H = [-1, -1]
while True:
    W, H = map(int, sys.stdin.readline().rstrip().split())
    if W == 0 or H == 0: break
    graph = []
    for _ in range(H):
        graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    visited = [[False for _ in range(W)] for _ in range(H)]

    result = 0
    for i in range(H):
        for j in range(W):
            if not visited[i][j] and graph[i][j]:
                dfs((i, j))
                result += 1
    print(result)

"""
5 4
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0
0 0
"""