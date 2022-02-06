# 텀 프로젝트
"""
이번 가을학기에 '문제 해결' 강의를 신청한 학생들은 텀 프로젝트를 수행해야 한다. 프로젝트 팀원 수에는 제한이 없다.
심지어 모든 학생들이 동일한 팀의 팀원인 경우와 같이 한 팀만 있을 수도 있다.
프로젝트 팀을 구성하기 위해, 모든 학생들은 프로젝트를 함께하고 싶은 학생을 선택해야 한다. (단, 단 한 명만 선택할 수 있다.)
혼자 하고 싶어하는 학생은 자기 자신을 선택하는 것도 가능하다.

학생들이(s1, s2, ..., sr)이라 할 때, r=1이고 s1이 s1을 선택하는 경우나,
1이 s2를 선택하고, s2가 s3를 선택하고,..., sr-1이 sr을 선택하고, sr이 s1을 선택하는 경우에만 한 팀이 될 수 있다.

예를 들어, 한 반에 7명의 학생이 있다고 하자. 학생들을 1번부터 7번으로 표현할 때, 선택의 결과는 다음과 같다.

1	2	3	4	5	6	7
3	1	3	7	3	4	6
위의 결과를 통해 (3)과 (4, 7, 6)이 팀을 이룰 수 있다. 1, 2, 5는 어느 팀에도 속하지 않는다.
주어진 선택의 결과를 보고 어느 프로젝트 팀에도 속하지 않는 학생들의 수를 계산하는 프로그램을 작성하라.
"""
import sys
from collections import deque

def dfs(start):
    checked = deque([start])
    stack = deque([start])
    visited[start] = True

    while stack:
        next = graph[stack.pop()]

        # 이미 방문한 노드라면
        # 1. 사이클(팀)일 경우
        # 2. 팀에 포함되지 않은 노드였을경우
        if visited[next]:
            # 시작점과 같다면 사이클이다.
            if next == start:
                for num in checked:
                    isTeamed[num] = True
            # 시작점과 다르다면
            else:
                # dfs 중에 이미 봤던 노드라면, 사이클이 형성되었다는 뜻
                if next in checked:
                    for num in list(checked)[checked.index(next):]:
                        isTeamed[num] = True
                # dfs 중에 봤던 노드가 아니라 새로운 노드라면, 이전 dfs에서 체크했다는 뜻
        else:
            stack.append(next)
            checked.append(next)
            visited[next] = True

# 사이클이 돈다면 그것은 팀이 된 것이다.
for _ in range(int(sys.stdin.readline().rstrip())):
    # 그래프 초기화
    N = int(sys.stdin.readline().rstrip())
    graph = [[] for _ in range(N+1)]
    sequence = list(map(int, sys.stdin.readline().rstrip().split()))
    for i in range(1, N+1):
        graph[i] = sequence[i-1]

    # 팀이 된 학생들을 체크하기 위한 변수 설정
    isTeamed = [True] + [False for _ in range(N)]
    visited = [True] + [False for _ in range(N)]

    for start in range(1, N+1):
        if not visited[start]:
            dfs(start)

    result = 0
    for i in isTeamed:
        if not i:
            result += 1
    print(result)


"""
1
3
2 3 2
ans

1
3
1 2 3

1
3
2 3 0

1
7
3 1 3 7 3 4 6
ans : 3

1
8
1 2 3 4 5 6 7 8
"""