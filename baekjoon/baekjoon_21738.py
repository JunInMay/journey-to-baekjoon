# 얼음깨기 펭귄
"""
도도는 심심해서 보드게임 카페에 갔다.
마침 평소에 즐겨 했던 얼음 깨기 펭귄의 업그레이드 버전으로 특수 얼음 깨기 펭귄 보드게임이 나와 직접 플레이해 보기로 결정했다.
특수 얼음 깨기 펭귄 게임은 특수 안경이 있어 특수 안경을 끼고 얼음들을 보면 얼음들 간의 연결 관계가 보인다.

특수 얼음 깨기 펭귄 게임에 있는 얼음의 종류로는 지지대의 역할을 하는 얼음과 일반 얼음 총 2가지의 얼음이 존재한다.
지지대의 역할을 하는 얼음의 경우, 빨간색으로 구분하여 볼 수 있으며 일반 얼음을 지탱해 주어 일반 얼음들이 깨지지 않도록 도와준다.
일반 얼음의 경우에는 1개의 지지대만이 연결되어 있어도 얼음이 깨지지 않지만 펭귄이 올라가 있는 얼음은 2개 이상의 지지대의 역할을 하는 얼음이 연결되어 있어야만 얼음이 깨지지 않는다.
이때, 지지대가 연결되어 있다는 것은 지지대로부터 서로 다른 일반 얼음들을 통해 연결 관계가 이어져 있는 것을 이야기한다.
특수 얼음 깨기 펭귄 게임에서 도도가 펭귄을 떨어뜨리지 않고 최대 몇 개의 얼음을 깰 수 있을까?
"""
import sys

sys.setrecursionlimit(500000)

N, S, P = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(now, count):
    if now == P:
        routes.append(count)
        return

    visited[now] = True
    for node in graph[now]:
        if not visited[node]:
            dfs(node, count + 1)


routes = []
visited = [False for _ in range(N + 1)]
for i in range(1, S + 1):
    dfs(i, 0)
print(N - (sum(sorted(routes)[:2]) + 1))

"""
23 6 12
1 9
1 10
10 12
2 13
13 11
11 12
3 8
8 7
8 12
5 19
5 14
14 12
6 20
6 21
20 15
15 12
4 18
4 17
17 16
16 12
7 22
7 23
res:18
ans:18

7 6 7
1 7
2 7
3 7
4 7
5 7
6 7

15 6 7
1 10
1 11
1 9
10 12
10 13
11 14
11 7
9 8
9 15
2 7
3 7
4 7
5 7
6 7

4 2 3
1 3
2 3
3 4

"""
