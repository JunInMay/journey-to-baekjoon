# DFS와 BFS
"""
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
"""
import sys

N, M, V = map(int, sys.stdin.readline().rstrip().split())

graph = {}
for i in range(1, N):
    graph[i] = []
for i in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a] = graph.get(a, []) + [b]
    graph[b] = graph.get(b, []) + [a]
for k, v in graph.items():
    graph[k] = sorted(v)

def dfs(now, visited):
    visited[now] = True
    print(now, end=' ')
    for i in graph[now]:
        if not visited[i]:
            dfs(i, visited)
    return None

from collections import deque

def bfs(start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for n in graph[v]:
            if not visited[n]:
                queue.append(n)
                visited[n] = True

dfs(V, [False for _ in range(N+1)])
print()
bfs(V, [False for _ in range(N+1)])