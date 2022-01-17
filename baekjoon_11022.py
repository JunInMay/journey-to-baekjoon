# A+B - 8
"""
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
"""
"""
5
1 1
2 3
3 4
9 8
5 2
Case #1: 1 + 1 = 2
Case #2: 2 + 3 = 5
Case #3: 3 + 4 = 7
Case #4: 9 + 8 = 17
Case #5: 5 + 2 = 7
"""

import sys
n = int(sys.stdin.readline().rstrip())

init_list = []
for i in range(n):
    a, b = list(map(int, sys.stdin.readline().rstrip().split()))
    init_list.append([a, b])

index = 1
for case in init_list:
    print(f"Case #{index}: {case[0]} + {case[1]} = {case[0]+case[1]}")
    index += 1