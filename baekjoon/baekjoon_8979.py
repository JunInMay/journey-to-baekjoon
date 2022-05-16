# 올림픽
"""
올림픽은 참가에 의의가 있기에 공식적으로는 국가간 순위를 정하지 않는다.
그러나, 많은 사람들이 자신의 국가가 얼마나 잘 하는지에 관심이 많기 때문에 비공식적으로는 국가간 순위를 정하고 있다.
두 나라가 각각 얻은 금, 은, 동메달 수가 주어지면, 보통 다음 규칙을 따라 어느 나라가 더 잘했는지 결정한다.

금메달 수가 더 많은 나라
금메달 수가 같으면, 은메달 수가 더 많은 나라
금, 은메달 수가 모두 같으면, 동메달 수가 더 많은 나라
각 국가는 1부터 N 사이의 정수로 표현된다. 한 국가의 등수는 (자신보다 더 잘한 나라 수) + 1로 정의된다.
만약 두 나라가 금, 은, 동메달 수가 모두 같다면 두 나라의 등수는 같다. 예를 들어, 1번 국가가 금메달 1개, 은메달 1개를 얻었고,
2번 국가와 3번 국가가 모두 은메달 1개를 얻었으며, 4번 국가는 메달을 얻지 못하였다면, 1번 국가가 1등, 2번 국가와 3번 국가가 공동 2등, 4번 국가가 4등이 된다.
이 경우 3등은 없다.

각 국가의 금, 은, 동메달 정보를 입력받아서, 어느 국가가 몇 등을 했는지 알려주는 프로그램을 작성하시오.
"""
import sys

N, K = map(int, sys.stdin.readline().rstrip().split())

medals = []
for _ in range(N):
    medals.append(list(map(int, sys.stdin.readline().rstrip().split())))

medals.sort(key=lambda x : (x[1], x[2], x[3]), reverse=True)

rank = 0
same_rank = 0
record_before = []
for medal in medals:
    record_now = medal[1:]
    if record_now != record_before:
        record_before = record_now
        rank += (1 + same_rank)
        same_rank = 0
    else:
        same_rank += 1

    if medal[0] == K:
        print(rank)
        break

"""
5 1
1 3 2 10
2 5 1 0
3 5 1 0
4 4 4 2
5 4 4 2


4 2
1 3 0 0
3 0 0 2
4 0 2 0
2 0 2 0
"""