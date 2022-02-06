# 반복수열
"""
다음과 같이 정의된 수열이 있다.

D[1] = A
D[n] = D[n-1]의 각 자리의 숫자를 P번 곱한 수들의 합
예를 들어 A=57, P=2일 때,
수열 D는 [57, 74(=52+72=25+49), 65, 61, 37, 58, 89, 145, 42, 20, 4, 16, 37, …]이 된다.
그 뒤에는 앞서 나온 수들(57부터가 아니라 58부터)이 반복된다.

이와 같은 수열을 계속 구하다 보면 언젠가 이와 같은 반복수열이 된다.
이때, 반복되는 부분을 제외했을 때, 수열에 남게 되는 수들의 개수를 구하는 프로그램을 작성하시오.
위의 예에서는 [57, 74, 65, 61]의 네 개의 수가 남게 된다.
"""
import math
import sys

def getNext(A, P):
    next = 0
    for exponent in range(math.floor(math.log10(A)), -1, -1):
        divisor = math.pow(10, exponent)
        quotient = A // divisor
        next += int(pow(quotient, P))
        A -= divisor * quotient

    return next

A, P = map(int, sys.stdin.readline().rstrip().split())
graph = {}
next = getNext(A, P)
graph[A] = [1, next]
index = 2
result = -1
while True:
    A = next
    try:
        graph[A] = graph[A]
        result = graph[A]
        break
    except:
        next = getNext(A, P)
        graph[A] = [index, next]
        index += 1
print(result[0]-1)
