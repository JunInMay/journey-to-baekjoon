# 조합 0의 개수
"""
$n \choose m$의 끝자리 $0$의 개수를 출력하는 프로그램을 작성하시오.
(조합 nCm)
"""
# idea
"""
boj 1676 팩토리얼 0의 개수 문제에서 알아봤던 것처럼 끝자리 0의 개수라는 것은
n!에 5가 얼마나 많이 인수로 들어가있는가를 알아보면 됐다.
이를 응용해서, 조합에서 끝자리 0의 개수를 알아봐야 하는 문제를 풀 수 있다.
조합 공식에 대해서 잘 몰랐지만, 찾아보니
nCm = n! / ((n-m)! * m!) 이라고 한다. 즉 nCm 에서 5의 개수를 세면 된다는 것이다.
그런데 n!에서 5의 개수라는 것은 5가 인수로 얼마나 들어가있느냐를 세는 것인데,
이를 (n-m)! * m! 으로 나눈다는 것은 (n-m)! * m! 라는 수 안에 들어있는 5의 개수만큼
n!의 5의 개수에서 빼준다는 말이다.
즉 f(n!) 를 n!에 들어있는 5의 개수라고 한다면
f(n! / ((n-m)! * m!)) = f(n!) - f((n-m)!) + f(m!) 이 되는 것이다.

--- 추가 ---
단순히 5의 개수만 세면 안된다. 끝자리 0의 개수는 사실 2x5의 개수를 세어야 한다.
그런데 케이스에 따라서 5의 개수보다 2의 개수가 많은 케이스, 2의 개수보다 5의 개수가 더 많은 케이스가 존재한다.
즉 2의 개수와 5의 개수 중 가장 적은 케이스가 답이 된다.
그러려면 2의 개수와 5의 개수를 모두 세어줘야 한다는 말이 된다.
"""
# 추가 내용과 관련된 케이스들
# case 12 3
# 결과 : 2는 2개, 5는 1개

# case 25 16
# 결과 : 2는 0개, 5는 2개

import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
candidates = [N, N-M, M]

def count_2_as_factor(num):
    result = 0
    while num >= 2:
        result += num // 2
        num //= 2

    return result

def count_5_as_factor(num):
    result = 0
    while num >= 5:
        result += num // 5
        num //= 5

    return result

results = []
for i in range(len(candidates)):
    temp = [count_2_as_factor(candidates[i]), count_5_as_factor(candidates[i])]
    results.append(temp)
result = [0, 0]
for i in range(2):
    result[i] = results[0][i] - (results[1][i] + results[2][i])
print(min(result))


