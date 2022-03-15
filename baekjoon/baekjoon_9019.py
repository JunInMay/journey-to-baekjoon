# DSLR
"""
네 개의 명령어 D, S, L, R 을 이용하는 간단한 계산기가 있다. 이 계산기에는 레지스터가 하나 있는데,
이 레지스터에는 0 이상 10,000 미만의 십진수를 저장할 수 있다. 각 명령어는 이 레지스터에 저장된 n을 다음과 같이 변환한다.
n의 네 자릿수를 d1, d2, d3, d4라고 하자(즉 n = ((d1 × 10 + d2) × 10 + d3) × 10 + d4라고 하자)

D: D 는 n을 두 배로 바꾼다. 결과 값이 9999 보다 큰 경우에는 10000 으로 나눈 나머지를 취한다. 그 결과 값(2n mod 10000)을 레지스터에 저장한다.
S: S 는 n에서 1 을 뺀 결과 n-1을 레지스터에 저장한다. n이 0 이라면 9999 가 대신 레지스터에 저장된다.
L: L 은 n의 각 자릿수를 왼편으로 회전시켜 그 결과를 레지스터에 저장한다. 이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d2, d3, d4, d1이 된다.
R: R 은 n의 각 자릿수를 오른편으로 회전시켜 그 결과를 레지스터에 저장한다. 이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d4, d1, d2, d3이 된다.
위에서 언급한 것처럼, L 과 R 명령어는 십진 자릿수를 가정하고 연산을 수행한다. 예를 들어서 n = 1234 라면 여기에 L 을 적용하면 2341 이 되고 R 을 적용하면 4123 이 된다.

여러분이 작성할 프로그램은 주어진 서로 다른 두 정수 A와 B(A ≠ B)에 대하여 A를 B로 바꾸는 최소한의 명령어를 생성하는 프로그램이다.
예를 들어서 A = 1234, B = 3412 라면 다음과 같이 두 개의 명령어를 적용하면 A를 B로 변환할 수 있다.

1234 →L 2341 →L 3412
1234 →R 4123 →R 3412

따라서 여러분의 프로그램은 이 경우에 LL 이나 RR 을 출력해야 한다.
n의 자릿수로 0 이 포함된 경우에 주의해야 한다. 예를 들어서 1000 에 L 을 적용하면 0001 이 되므로 결과는 1 이 된다. 그러나 R 을 적용하면 0100 이 되므로 결과는 100 이 된다.
"""
import sys
from collections import deque


def doD(num):
    return num * 2 % 10000


def doS(num):
    return num - 1 if num > 0 else 9999


def doL(num):
    sNum = str(num)
    n = len(sNum)
    if n < 4:
        sNum = "0"*(4-n) + sNum

    return int(sNum[1:4] + sNum[:1])


def doR(num):
    sNum = str(num)
    n = len(sNum)
    if n < 4:
        sNum = "0"*(4-n) + sNum

    return int(sNum[4-1] + sNum[:4-1])


def getDSLR(num):
    return [doD(num), doS(num), doL(num), doR(num)]


def bfs(start, goal):
    queue = deque([(start, "")])
    visited = [False for _ in range(10000)]

    while queue:
        node, history = queue.popleft()
        if node == goal:
            return history
        for i in range(4):
            if not visited[graph[node][i]]:
                visited[graph[node][i]] = True
                queue.append((graph[node][i], history+DSLR[i]))


graph = []
DSLR = ["D", "S", "L", "R"]
for n in range(10000):
    graph.append(getDSLR(n))

for _ in range(int(sys.stdin.readline().rstrip())):
    s, g = map(int, sys.stdin.readline().rstrip().split())
    print(bfs(s, g))