# 숨바꼭질
"""
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.
수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.
"""
import sys
from collections import deque

graph = [[] for _ in range(100001)]
visited = [False for _ in range(len(graph))]


for i in range(len(graph)):
    if i > 0:
        graph[i].append(i-1)
    if i < 100000:
        graph[i].append(i+1)
    if i > 0 and i < 50001:
        graph[i].append(i*2)



N, K = map(int, sys.stdin.readline().rstrip().split())
result = 0


def bfs(start, goal):
    global result
    queue = deque([(start, 0)])

    while queue:
        next, cost = queue.popleft()
        if next == goal:
            result = cost
            return
        for node in graph[next]:
            if not visited[node]:
                visited[node] = True
                queue.append((node, cost+1))

    return

bfs(N, K)
print(result)

"""
511 700
111 300
111 150
"""
