# 수 정렬하기
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
# 좋은 정렬 알고리즘이 많지만, 문제에서 제시한 대로 n^2 알고리즘(선택 정렬)을 사용.

import sys
iteration = int(sys.stdin.readline().rstrip())

array = []
for i in range(iteration):
    array.append(int(sys.stdin.readline().rstrip()))

for i in range(iteration):
    for j in range(iteration):
        if array[i] < array[j]:
            array[i], array[j] = array[j], array[i]

for i in range(iteration):
    print(array[i])