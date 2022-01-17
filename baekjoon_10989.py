# 수 정렬하기 3
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
# 메모리 초과 오류(계수정렬 aka counting sort 확인해야 함.)

import sys

num = int(sys.stdin.readline().rstrip())

count = [0]*10001
for i in range(num):
    input = int(sys.stdin.readline().rstrip())
    count[input] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i)