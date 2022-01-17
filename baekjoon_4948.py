# 베르트랑 공준
"""
베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다.
이 명제는 조제프 베르트랑이 1845년에 추측했고, 파프누티 체비쇼프가 1850년에 증명했다.
예를 들어, 10보다 크고, 20보다 작거나 같은 소수는 4개가 있다.
(11, 13, 17, 19) 또, 14보다 크고, 28보다 작거나 같은 소수는 3개가 있다. (17,19, 23)
자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오.
"""
import sys
case = -1
cases = []
while case != 0:
    case = int(sys.stdin.readline().rstrip())
    if case != 0:
        cases.append(case)

def sieve(n):
    limit = (n*2)**(1/2)
    for prime in range(2, 3 if limit < 2 else round(limit)+1):
        index_scalar = 1
        while prime*index_scalar <= 2*n:
            index = prime*index_scalar-(n+1)
            if index >= 0 and index < len(scope) and index_scalar != 1:
                scope[index] = False
            index_scalar += 1

for case in cases:
    scope = [True for n in range(case)]
    result = sieve(case)
    lis = [n + case + 1 for n in range(case)]
    print(sum(scope))
