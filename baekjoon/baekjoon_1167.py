# 트리의 지름
"""
트리의 지름이란, 트리에서 임의의 두 점 사이의 거리 중 가장 긴 것을 말한다. 트리의 지름을 구하는 프로그램을 작성하시오.
"""
"""
트리의 지름 증명 참조
https://blog.myungwoo.kr/112
"""
import sys
sys.setrecursionlimit(100000)

# 그래프 초기화
N = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
for _ in range(N):
    line = list(map(int, sys.stdin.readline().rstrip().split()))
    edges = line[1:-1]
    for i in range(0, len(edges), 2):
        graph[line[0]].append((edges[i], edges[i+1]))

# 한 노드를 입력하면, 그 노드에 연결된 간선들을 dfs로 탐색하는 거리의 최대값을 리턴하는 함수
def dfs(start):
    temp = result = 0
    num = start
    visited[start] = True

    for elem in graph[start]:
        node = elem[0]
        distance = elem[1]
        if not visited[node]:
            value, n = dfs(node)
            result = max(result, value + distance)
            if result != temp:
                num = n
            temp = result

    return result, num

result = []
node = dfs(1)[1]
visited = [False for _ in range(N+1)]
print(dfs(node)[0])

"""
10
1 3 2 6 3 7 4 8 5 -1
2 4 4 -1
3 1 2 4 3 -1
4 2 4 3 3 5 6 -1
5 4 6 -1
6 1 3 9 10 -1
7 1 4 10 22 -1
8 1 5 -1
9 6 10 -1
10 7 22 -1

6
1 2 1 3 2 4 3 5 4 6 5 -1
2 1 1 -1
3 1 2 -1
4 1 3 -1
5 1 4 -1
6 1 5 -1

2
1 2 3 -1
2 1 3 -1
"""

"""
4
1 2 5 3 9 -1
2 1 5 -1
3 1 9 4 8 -1
4 3 8 -1
"""
"""
6
1 2 3 -1
2 1 3 5 3 3 5 -1
3 2 5 4 7 -1
4 3 7 -1
5 2 3 6 5 -1
6 5 5 -1

답 : 20

4
1 2 7 3 2 -1
2 1 7 -1
3 1 2 4 3 -1
4 3 3 -1

답 : 12

5
1 2 7 3 2 5 10 -1
2 1 7 -1
3 1 2 4 3 -1
4 3 3 -1
5 1 10 -1

답 : 17
"""