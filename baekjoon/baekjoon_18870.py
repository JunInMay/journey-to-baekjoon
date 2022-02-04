# 좌표 압축
"""
수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.
Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.
X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.
"""
import sys

N = int(sys.stdin.readline().rstrip())
sequence = list(map(int, sys.stdin.readline().rstrip().split()))

mapping = {}
for num in sequence:
    mapping[num] = -1

merged_sequence = sorted(sequence)
before = float('-inf')

count = 0
for i in range(len(merged_sequence)):
    if before != merged_sequence[i]:
        mapping[merged_sequence[i]] = count
        before = merged_sequence[i]
        count += 1
    else: continue

print(*[mapping[x] for x in sequence])