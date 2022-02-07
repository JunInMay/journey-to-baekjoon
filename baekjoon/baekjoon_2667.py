# 단지번호붙이기
"""
<그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다.
철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다.
여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다.
<그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고,
각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.
"""
import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
init_sequence = []
for _ in range(N):
    init_sequence.append(list(map(int, sys.stdin.readline().rstrip())))

# 그래프 초기화
graph = [[[] for _ in range(N)] for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        # 1이면, 상하좌우 판별해야 함
        if init_sequence[i][j]:
            # 자기 자신 그래프로 넣기
            graph[i][j].append((i, j))
            # 상 판별, i == 0이면 상을 판별할 수 없음
            if i != 0:
                if init_sequence[i-1][j]:
                    graph[i][j].append((i-1, j))
            # 하 판별, i == N-1이면 하를 판별할 수 없음
            if i != N-1:
                if init_sequence[i+1][j]:
                    graph[i][j].append((i+1, j))
            # 좌 판별, j == 0이면 좌를 판별할 수 없음
            if j != 0:
                if init_sequence[i][j-1]:
                    graph[i][j].append((i, j-1))
            # 좌 판별, j == N-1이면 좌를 판별할 수 없음
            if j != N-1:
                if init_sequence[i][j+1]:
                    graph[i][j].append((i, j+1))

result = []
for i in range(N):
    for j in range(N):
        # 그래프에 무언가 있다면(노드라면)
        if graph[i][j]:
            # 그리고 거기에 방문하지 않았을 경우
            if not visited[i][j]:
                temp = 1
                start = (i, j)
                stack = deque([(i, j)])
                visited[i][j] = True
                while stack:
                    next = stack.pop()
                    for coordinate in graph[next[0]][next[1]]:
                        x = coordinate[0]
                        y = coordinate[1]
                        if not visited[x][y]:
                            visited[x][y] = True
                            stack.append((x, y))
                            temp += 1
                result.append(temp)

print(len(result))
for line in sorted(result):
    print(line)

# print(graph)
"""
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000

3
010
101
010
"""