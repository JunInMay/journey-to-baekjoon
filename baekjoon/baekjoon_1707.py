# 이분 그래프
"""
그래프의 정점의 집합을 둘로 분할하여, 각 집합에 속한 정점끼리는 서로 인접하지 않도록 분할할 수 있을 때,
그러한 그래프를 특별히 이분 그래프 (Bipartite Graph) 라 부른다.
그래프가 입력으로 주어졌을 때, 이 그래프가 이분 그래프인지 아닌지 판별하는 프로그램을 작성하시오.
"""
import sys
from collections import deque

for _ in range(int(sys.stdin.readline().rstrip())):
    V, E = map(int, sys.stdin.readline().rstrip().split())
    graph = [[] for _ in range(V+1)]
    visited = [True] + [False for _ in range(V)]
    for _ in range(E):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        graph[a].append(b)
        graph[b].append(a)

    flag = 0
    for start in range(1, len(visited)):
        if not visited[start]:
            stack = deque([(start, 1)])
            visited[start] = 1
            while stack:
                elem = stack.pop()
                v = elem[0]
                color = elem[1]
                if color == 1:
                    next_color = 2
                else:
                    next_color = 1

                for node in graph[v]:
                    if not visited[node]:
                        stack.append((node, next_color))
                        visited[node] = next_color
                    elif visited[node] != next_color:
                        flag = 1
                        break
                if flag:
                    break
        if flag:
            break
    if flag:
        print("NO")
    else:
        print("YES")

"""
2
3 2
1 3
2 3
4 4
1 2
2 3
3 4
4 2

2
3 0
5 5
1 2
2 3
3 4
4 5
5 1

2
5 4
1 2
3 4
4 5
1 5
5 4
1 2
2 3
3 4
4 5

1
8 12
1 2
1 3
1 5
2 6
2 4
3 7
3 4
4 8
5 6
5 7
6 8
7 8
ans : yes
"""