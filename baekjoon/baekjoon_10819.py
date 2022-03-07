# 차이를 최대로
"""
N개의 정수로 이루어진 배열 A가 주어진다. 이때, 배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램을 작성하시오.

|A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|
"""
import sys


def get_result_of_expression(li):
    res = 0
    for i in range(len(li) - 1):
        res += abs(li[i] - li[i + 1])

    return res


def make_permutation(li, origin=[]):
    if len(li) == 0:
        candidates.append(origin)

    temp = origin[:]
    for i in range(len(li)):
        next = li[:i] + li[i + 1:]
        temp += [li[i]]
        make_permutation(next, temp)
        temp = origin[:]


N = int(sys.stdin.readline().rstrip())
li = list(map(int, sys.stdin.readline().rstrip().split()))
candidates = []
make_permutation(li)

res = float("-inf")
for cand in candidates:
    res = max(res, get_result_of_expression(cand))
print(res)

"""
3
1 2 3
6
20 1 15 8 4 10
"""
