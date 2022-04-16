"""
# 24883
import sys

if sys.stdin.readline().rstrip() in ['N', 'n']:
    print("Naver D2")
else:
    print("Naver Whale")
"""

import sys

input_number = sys.stdin.readline().rstrip()
F = int(sys.stdin.readline().rstrip())

for i in range(100):
    if i < 10:
        res = "0" + str(i)
    else:
        res = str(i)
    N = int(input_number[:-2] + res)
    if N % F == 0:
        print(res)
        break
