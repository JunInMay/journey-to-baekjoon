# 외판원 순회 2
"""
외판원 순회 문제는 영어로 Traveling Salesman problem (TSP) 라고 불리는 문제로
computer science 분야에서 가장 중요하게 취급되는 문제 중 하나이다.
여러 가지 변종 문제가 있으나, 여기서는 가장 일반적인 형태의 문제를 살펴보자.

1번부터 N번까지 번호가 매겨져 있는 도시들이 있고, 도시들 사이에는 길이 있다.
(길이 없을 수도 있다) 이제 한 외판원이 어느 한 도시에서 출발해 N개의 도시를 모두 거쳐 다시 원래의 도시로 돌아오는 순회 여행 경로를 계획하려고 한다.
단, 한 번 갔던 도시로는 다시 갈 수 없다. (맨 마지막에 여행을 출발했던 도시로 돌아오는 것은 예외) 이런 여행 경로는 여러 가지가 있을 수 있는데,
가장 적은 비용을 들이는 여행 계획을 세우고자 한다.

각 도시간에 이동하는데 드는 비용은 행렬 W[i][j]형태로 주어진다. W[i][j]는 도시 i에서 도시 j로 가기 위한 비용을 나타낸다.
비용은 대칭적이지 않다. 즉, W[i][j] 는 W[j][i]와 다를 수 있다. 모든 도시간의 비용은 양의 정수이다. W[i][i]는 항상 0이다. 경우에 따라서 도시 i에서 도시 j로 갈 수 없는 경우도 있으며 이럴 경우 W[i][j]=0이라고 하자.

N과 비용 행렬이 주어졌을 때, 가장 적은 비용을 들이는 외판원의 순회 여행 경로를 구하는 프로그램을 작성하시오.
"""
"""
실패...?
그런데 자바로 해당 로직 그대로 구현하니까 통과함
파이썬 손절하자..
"""


import sys

def seek_way(start, now, visited, cost):
    if len(visited) == len(costs) and start == now:
        candidates.append(cost)
        return None

    for i in range(len(costs[now])):
        if i in visited:
            continue
        else:
            if costs[now][i] != 0:
                visited.append(i)
                seek_way(start, i, visited, cost+costs[now][i])
                visited.pop()


costs = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(int(sys.stdin.readline().rstrip()))]
candidates = []
for i in range(len(costs)):
    seek_way(i, i, [], 0)

print(candidates)

"""
2
0 2
2 0
"""
