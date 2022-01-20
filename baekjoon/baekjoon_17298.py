# 오큰수
"""
크기가 N인 수열 A = A1, A2, ..., AN이 있다.
수열의 각 원소 Ai에 대해서 오큰수 NGE(i)를 구하려고 한다.
Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다. 그러한 수가 없는 경우에 오큰수는 -1이다.

예를 들어, A = [3, 5, 2, 7]인 경우 NGE(1) = 5, NGE(2) = 7, NGE(3) = 7, NGE(4) = -1이다.
A = [9, 5, 4, 8]인 경우에는 NGE(1) = -1, NGE(2) = 8, NGE(3) = 8, NGE(4) = -1이다.
"""
"""
파이썬에서
"""
import sys
N = int(sys.stdin.readline().rstrip())
sequence = list(map(int, sys.stdin.readline().rstrip().split()))
NGE = [-1]
candidates = [sequence[-1]]

for i in range(N-2, -1, -1):
    while candidates:
        top = candidates[-1]
        if sequence[i] < top:
            NGE.append(top)
            candidates.append(sequence[i])
            break
        else: candidates.pop()
    if len(candidates) == 0:
        candidates = [sequence[i]]
        NGE.append(-1)
print(*NGE[::-1])

import sys
N = int(sys.stdin.readline().rstrip())
sequence = list(map(int, sys.stdin.readline().rstrip().split()))
NGE = []
candidates = []

maxi = float('-inf')
for i in range(N-1, -1, -1):
    if len(candidates) == 0:
        NGE.append(-1)
        candidates.append(sequence[i])
        maxi = max(sequence[i], maxi)
    else:
        if sequence[i] >= maxi:
            candidates = [sequence[i]]
            NGE.append(-1)
            maxi = sequence[i]
            continue
        for j in range(len(candidates)):
            top = candidates[-1]
            if sequence[i] < top:
                NGE.append(top)
                candidates.append(sequence[i])
                break
            candidates.pop()
print(*NGE[::-1])

"""
6
6 3 5 1 2 7
7 5 7 2 7 -1
7
4 3 2 1 2 3 4
4
3 2 5 3
5 5 -1 -1
"""