# Половина
"""
У доброжелательного Даниила есть несколько яблок.
В силу своей природной доброжелательности, каждый раз, когда он встречает какого-либо своего друга, он смотрит на яблоки,
которые у него есть и отдает другу половину.

Но Даниил не одинаково любит всех своих друзей, поэтому некоторым из них он отдает половину яблока,
а некоторым --- половину имеющихся у него яблок. При этом с глазомером у Даниила не так хорошо, как со щедростью,
и делить яблоки более, чем на две части, у него не получается. Поэтому, если он встречает друга, а у него нецелое число яблок,
то он вынужден отдать половину яблока.

Утром у Даниила было $n$ яблок, а за день Даниил встретил $k$ друзей. Выясните, сколько яблок у него могло остаться вечером.
"""
"""
영어로 번역해서 읽는 것이 편함...
파이썬 시간초과, C++로 재도전해야 할듯함, 맞춘 사람들이 전부 C++이고, java나 python은 한 명도 없음
"""
import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
memo = [[[0] for _ in range(1001)], [[1],[0.5]]+[[0] for _ in range(999)]]

import time
start = time.time()
for number in range(2, N+1):
    base = [[number], [number/2, number-0.5]]
    for i in range(2, K+1):
        # temp = []
        # if number % 2 > 0:
        #     temp += memo[number//2][i-2] + memo[number-1][i-2]
        # else:
        #     temp += memo[number//2][i-1] + memo[number-1][i-2]
        # base.append(list(set(temp)))

        if number % 2 > 0:
            base.append(list(set(memo[number//2][i-2] + memo[number-1][i-2])))
        else:
            base.append(list(set(memo[number//2][i-1] + memo[number-1][i-2])))
    memo.append(base)
print(f"시간 : {time.time()-start} 초")

print(len(memo[N][K]))
print(*sorted(memo[N][K]))