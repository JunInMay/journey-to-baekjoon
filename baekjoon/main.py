# 수 정렬하기 2
"""
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
"""

import sys

num = int(sys.stdin.readline().rstrip())

list = []
for i in range(num):
    list.append(int(sys.stdin.readline().rstrip()))

list.sort()
print(list)