# 타노스
"""
어느 날, 타노스는 0과 1로 이루어진 문자열 $S$를 보았다.
신기하게도, $S$가 포함하는 0의 개수와 $S$가 포함하는 1의 개수는 모두 짝수라고 한다.
갑자기 심술이 난 타노스는 $S$를 구성하는 문자 중 절반의 0과 절반의 1을 제거하여 새로운 문자열 $S'$를 만들고자 한다. $S'$로 가능한 문자열 중 사전순으로 가장 빠른 것을 구하시오.
"""
import sys

text = list(map(int, list(sys.stdin.readline().rstrip())))
zero_count = text.count(0)
one_count = text.count(1)

text = text[::-1]
count = 0
temp = []
for character in text:
    if character == 0 and count < zero_count/2:
        count += 1
        continue
    else:
        temp.append(character)

text = temp[::-1]
temp = []
count = 0
for character in text:
    if character == 1 and count < one_count/2:
        count += 1
        continue
    else:
        temp.append(character)

for t in temp:
    print(t, end="")

"""
00110000
"""