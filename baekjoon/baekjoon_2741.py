# N 찍기
# 자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

import sys

n = int(sys.stdin.readline().rstrip())

for i in range(1, n+1):
    print(i)