# 한수
"""
어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다.
등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.
"""
import sys

sequence = int(sys.stdin.readline().rstrip())


def check_arithmetic_sequence(num):
    num_sequence = list(map(int, list(str(num))))
    l = len(str(num))
    if l == 1:
        return 1
    elif l >= 2:
        diff = num_sequence[l-1] - num_sequence[l-2]


    for i in range(l-1, 0, -1):
        F = num_sequence[i]
        S = num_sequence[i-1]
        if F-S != diff:
            return 0
    return 1


count = 0
for num in range(1, sequence+1):
    count += check_arithmetic_sequence(num)

print(count)