# 다리 만들기
"""
여러 섬으로 이루어진 나라가 있다. 이 나라의 대통령은 섬을 잇는 다리를 만들겠다는 공약으로 인기몰이를 해 당선될 수 있었다.
하지만 막상 대통령에 취임하자, 다리를 놓는다는 것이 아깝다는 생각을 하게 되었다.
그래서 그는, 생색내는 식으로 한 섬과 다른 섬을 잇는 다리 하나만을 만들기로 하였고, 그 또한 다리를 가장 짧게 하여 돈을 아끼려 하였다.

이 나라는 N×N크기의 이차원 평면상에 존재한다. 이 나라는 여러 섬으로 이루어져 있으며,
섬이란 동서남북으로 육지가 붙어있는 덩어리를 말한다. 다음은 세 개의 섬으로 이루어진 나라의 지도이다.

위의 그림에서 색이 있는 부분이 육지이고, 색이 없는 부분이 바다이다. 이 바다에 가장 짧은 다리를 놓아 두 대륙을 연결하고자 한다.
가장 짧은 다리란, 다리가 격자에서 차지하는 칸의 수가 가장 작은 다리를 말한다. 다음 그림에서 두 대륙을 연결하는 다리를 볼 수 있다.

물론 위의 방법 외에도 다리를 놓는 방법이 여러 가지 있으나,
위의 경우가 놓는 다리의 길이가 3으로 가장 짧다(물론 길이가 3인 다른 다리를 놓을 수 있는 방법도 몇 가지 있다).

지도가 주어질 때, 가장 짧은 다리 하나를 놓아 두 대륙을 연결하는 방법을 찾으시오.
"""
import sys
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def check_island(start):
    queue = deque([start])

    while queue:
        node = queue.popleft()
        y, x = node
        visited[y][x] = numbering

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= nx < N and 0 <= ny < N and init_graph[ny][nx] and not visited[ny][nx]:
                visited[ny][nx] = numbering
                queue.append((ny, nx))

def sail(start):
    y, x = start
    queue = deque([start])
    visited[y][x] = 1
    numbering = graph[y][x]

    while queue:
        node = queue.popleft()
        y, x = node

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx]:
                if graph[ny][nx] and graph[ny][nx] != numbering:
                    return visited[y][x]
                elif not graph[ny][nx]:
                    visited[ny][nx] = visited[y][x] + 1
                    queue.append((ny, nx))

N = int(sys.stdin.readline().rstrip())

init_graph = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
numbering = -1
for i in range(N):
    for j in range(N):
        if not visited[i][j] and init_graph[i][j]:
            check_island((i, j))
            numbering -= 1

graph = visited
result = []
for i in range(N):
    for j in range(N):
        if graph[i][j]:
            visited = [[0 for _ in range(N)] for _ in range(N)]
            res = sail((i, j))
            if res:
                result.append(res)
print(min(result)-1)
"""
3
1 1 0
0 0 0
0 0 1

5
1 1 1 0 0
1 0 1 0 0
1 1 1 0 0
0 0 0 0 0
0 0 0 0 1

2
1 0
0 1

4
1 1 1 1
1 1 1 1
1 1 1 0
1 1 0 1
"""