# 물통
"""
각각 부피가 A, B, C(1≤A, B, C≤200) 리터인 세 개의 물통이 있다.
처음에는 앞의 두 물통은 비어 있고, 세 번째 물통은 가득(C 리터) 차 있다.
이제 어떤 물통에 들어있는 물을 다른 물통으로 쏟아 부을 수 있는데, 이때에는 한 물통이 비거나, 다른 한 물통이 가득 찰 때까지 물을 부을 수 있다.
이 과정에서 손실되는 물은 없다고 가정한다.

이와 같은 과정을 거치다보면 세 번째 물통(용량이 C인)에 담겨있는 물의 양이 변할 수도 있다. 첫 번째 물통(용량이 A인)이 비어 있을 때,
세 번째 물통(용량이 C인)에 담겨있을 수 있는 물의 양을 모두 구해내는 프로그램을 작성하시오.
"""
import sys
from collections import deque


# 숫자를 3글자 문자열로 만들기 e.g. 3 -> 003, 10 -> 010
def makeThreeDigits(num):
    return "0" * (3 - len(str(num))) + str(num)


# 문자열을 3개씩 잘라서 숫자로 만들기 e.g. 010020100 -> [10, 20, 100]
def getElements(text):
    return [int(text[i * 3:(i + 1) * 3]) for i in range(3)]


# 현재 상태에서(문자열) 시작 지점에서 목표 지점으로 물 붓기
def pour(now, start, goal):
    elements = getElements(now)
    sIndex = indexes[start]
    gIndex = indexes[goal]
    # 목표 지점에 여유가 있으면
    if elements[gIndex] < limits[goal]:
        value = min(limits[goal] - elements[gIndex], elements[sIndex])
        elements[gIndex] += value
        elements[sIndex] -= value
    A, B, C = elements
    return makeThreeDigits(A) + makeThreeDigits(B) + makeThreeDigits(C)


def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        node = queue.popleft()
        A, B, C = getElements(node)
        if A == 0:
            results.append(C)
        for s, g in operation:
            # 다음 문자열
            nText = pour(node, s, g)

            if not visited.get(nText):
                visited[nText] = True
                queue.append(nText)

    return None


# 명령어 (C에서 B로 붓기, C에서 A로 붓기... A에서 C로 붓는 동작, B에서 A로 붓는 동작은 필요가 없음)
operation = [("C", "B"), ("C", "A"), ("A", "B"), ("B", "C")]

# A, B, C에 들어갈 수 있는 최대 용량
limits = {}
limits["A"], limits["B"], limits["C"] = map(int, sys.stdin.readline().rstrip().split())

# pour 함수에서 인덱스 제공용
indexes = {"A": 0, "B": 1, "C": 2}

# 답
results = []

# 방문 체크용
visited = {}

# A, B가 모두 0리터고 C만 최대치로 시작
bfs("000000" + makeThreeDigits(limits["C"]))

print(*sorted(results))
