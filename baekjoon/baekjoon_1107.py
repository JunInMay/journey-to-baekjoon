# 리모컨
"""
수빈이는 TV를 보고 있다. 수빈이는 채널을 돌리려고 했지만, 버튼을 너무 세게 누르는 바람에, 일부 숫자 버튼이 고장났다.

리모컨에는 버튼이 0부터 9까지 숫자, +와 -가 있다. +를 누르면 현재 보고있는 채널에서 +1된 채널로 이동하고,
-를 누르면 -1된 채널로 이동한다. 채널 0에서 -를 누른 경우에는 채널이 변하지 않고, 채널은 무한대 만큼 있다.

수빈이가 지금 이동하려고 하는 채널은 N이다. 어떤 버튼이 고장났는지 주어졌을 때,
채널 N으로 이동하기 위해서 버튼을 최소 몇 번 눌러야하는지 구하는 프로그램을 작성하시오.

수빈이가 지금 보고 있는 채널은 100번이다.
"""
import sys

def check(num):
    for character in str(num):
        if is_defected[int(character)]:
            return False
    return True

# 처음에 내 채널은 100이야. 그러면, 숫자버튼을 누르지 않고 Goal로 간다고 했을 때 + 랑 -버튼을 눌러야 하는 횟수는?
# abs(Goal - 100)
Goal = int(sys.stdin.readline().rstrip())
is_defected = [False for _ in range(10)]
N = int(sys.stdin.readline().rstrip())

if N != 0:
    for num in list(map(int, sys.stdin.readline().rstrip().split())):
        is_defected[num] = True

result = abs(Goal - 100)

for i in range(max(Goal*2+1, 100)):
    if not check(i):
        continue
    result = min(result, abs(Goal-i) + len(str(i)))

print(result)

"""
10
9
0 1 2 3 4 5 6 7 8
"""