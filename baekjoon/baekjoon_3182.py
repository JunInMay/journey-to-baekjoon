# 한동이는 공부가 하기 싫어!
"""
H-ALGO 회원인 한동이는 공부하는것을 좋아하지 않는다. 하지만 약삭빠르게도 한동이는 공부도 하지 않으면서 어려운 시험을 통과하고 싶어한다.

그러던 와중 어느 날, 한동이의 동기가 한동이에게 선배들 중 누군가가 시험의 답을 알고있다는 꿀정보를 알려주었다.
하지만 안타깝게도 그 정보는 사실이 아니어서 선배들조차도 정답은 알지 못하고 다른 누군가가 알고 있을거 같다는 정보만 알고 있는 것이었다.

한동이는 택민이에게 시험 정답을 물어보았다. 택민이는 답을 모른다고 했지만 택민이는 상준이가 답을 알고 있을 것 같다고 하였다.
그 후, 한동이는 상준이에게 물어보고 그리고...

어느 순간 한동이는 아무리 이걸 해도 자신에게 도움이 되지 않는것을 깨닫고 굉장히 슬퍼졌다.
하지만 그는 이걸 함으로써 많은 선배들과 인맥을 쌓을 수 있고, 이게 언젠가 큰 도움이 될 것이라는 것을 깨달았다!

당신의 목표는 한동이가 한 사람에게만 시험문제를 물어볼 수 있다고 할 때,
최대한 많은 선배들을 만날 수 있게 하기 위해서 누구에게 시험문제를 물어 볼 것인지를 알려주는 것이다.
"""
import sys

graph = [0] + [int(sys.stdin.readline().rstrip()) for _ in range(int(sys.stdin.readline().rstrip()))]


def dfs(now):
    global count

    count += 1
    visited[now] = True
    if not visited[graph[now]]:
        dfs(graph[now])


search_counts = []
for i in range(1, len(graph)):
    visited = [False for _ in range(len(graph))]
    count = 0
    dfs(i)
    search_counts.append(count)

print(search_counts.index(max(search_counts))+1)