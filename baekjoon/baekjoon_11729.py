# 하노이 탑 이동 순서
"""
세 개의 장대가 있고 첫 번째 장대에는 반경이 서로 다른 n개의 원판이 쌓여 있다. 각 원판은 반경이 큰 순서대로 쌓여있다. 이제 수도승들이 다음 규칙에 따라 첫 번째 장대에서 세 번째 장대로 옮기려 한다.

한 번에 한 개의 원판만을 다른 탑으로 옮길 수 있다.
쌓아 놓은 원판은 항상 위의 것이 아래의 것보다 작아야 한다.
이 작업을 수행하는데 필요한 이동 순서를 출력하는 프로그램을 작성하라. 단, 이동 횟수는 최소가 되어야 한다.

아래 그림은 원판이 5개인 경우의 예시이다.
"""
"""
문제 팁
나중에 찾아볼 수 있어서 팁을 적는다.
하노이의 탑 문제는 divide and conquer 방식으로 나눌 수 있는 문제다.
생각해보면 하노이의 탑을 가장 최적의 방법으로 풀기위한 절대적인 필요조건을 생각해낼 수 있다.
n개의 원판이 있는 하노이의 탑 문제를 생각해보자.
1번 기둥에 있는 n개의 원판을 모두 3번 기둥으로 옮기려면 전제 조건이 필요하다.
n번 원판을 3번 기둥으로 옮기고 나서 그 위에 나머지 원판들을 쌓아야 한다는 것이다.
그러기 위해선 어떻게 해야 할까?
처음 상태(1번 원판부터 n번 원판까지 차례대로 쌓여져 있는 상태)에서 맨 밑에 깔린 n번 원판을 3번 기둥으로 옮기려면 어떻게 해야 할까?
당연한 이야기지만 n번 원판 위에 있는 1부터 n-1번까지의 원판들을 2번 기둥으로 옮겨야 한다.
그 다음엔 1번 기둥에 있는 n번 원판을 3번 기둥으로 옮기면 되고, 그 다음엔 어떻게 하면 될까?
또 당연한 이야기지만 2번 기둥에 있는 1부터 n-1번까지의 원판들을 3번 기둥으로 옮기면 된다.
한 가지 팁이 숨겨져있지만 이 정도 내용으로도 숨겨진 팁을 찾고, 문제를 풀 수 있을 것이라 생각한다.
"""

import sys

num = int(sys.stdin.readline().rstrip())
routes = []

def hanoi(start, end, plates):
    global routes
    for_other = start + end
    if for_other == 3: another = 3
    elif for_other == 4: another = 2
    else: another = 1

    if plates == 1:
        routes.append(f"{start} {end}")
        return None

    hanoi(start, another, plates-1)
    routes.append(f"{start} {end}")
    hanoi(another, end, plates-1)

    return None

hanoi(1, 3, num)

print(len(routes))
for route in routes:
    print(route)