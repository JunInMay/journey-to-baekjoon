# A+B - 7
"""
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
"""

import sys

times = int(sys.stdin.readline().rstrip())

cases = []
for i in range(times):
    cases.append(sum(list(map(int, sys.stdin.readline().rstrip().split()))))

for i in range(len(cases)):
    print(f"Case #{i+1}: {cases[i]}")
