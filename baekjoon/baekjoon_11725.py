# 트리의 부모 찾기
"""
루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.
"""
import sys
import collections

N = int(sys.stdin.readline().rstrip())
tree = [[]for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    tree[a].append(b)
    tree[b].append(a)
visited = [False for _ in range(N+1)]

def dfs(start):
    visited[start] = True
    stack = collections.deque([start])

    while stack:
        check = stack.pop()
        for elem in tree[check]:
            if not visited[elem]:
                stack.append(elem)
                visited[elem] = check
dfs(1)
for i in range(2, N+1):
    print(visited[i])