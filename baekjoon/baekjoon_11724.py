# 연결 요소의 개수
"""
첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2)
둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.
"""
import sys

graph = {}
N, M = map(int, sys.stdin.readline().rstrip().split())

for i in range(1, N+1):
    graph[i] = []
for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a] = graph[a]+[b]
    graph[b] = graph[b]+[a]
for v in graph.values():
    v = v.sort()

visited = [True] + [False for _ in range(N)]

from collections import deque

def bfs(now, visited):
    visited[now] = True
    queue = deque([now])
    while queue:
        v = queue.popleft()
        for node in graph[v]:
            if not visited[node]:
                visited[node] = True
                queue.append(node)

    return None

result = 0
for node in range(1, len(visited)):
    if not visited[node]:
        bfs(node, visited)
        result += 1

print(result)