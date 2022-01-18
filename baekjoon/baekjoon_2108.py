# 통계학
"""
수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.

산술평균 : N개의 수들의 합을 N으로 나눈 값
중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
최빈값 : N개의 수들 중 가장 많이 나타나는 값
범위 : N개의 수들 중 최댓값과 최솟값의 차이
N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.
"""

import sys

n = int(sys.stdin.readline().rstrip())

# 계수정렬(counting sort)
def counting_sort(li, num_range=4000):
    base_index = num_range
    min_index = num_range * -1
    count = [0] * (num_range * 2 + 1)

    sorted = []
    for element in li:
        count[base_index+element] += 1

    value = min_index
    for element in count:
        for i in range(element):
            sorted.append(value)
        value += 1

    return sorted, count

# 값 받고 계수정렬로 정렬된 리스트 반환
init_list = []
for i in range(n):
    init_list.append(int(sys.stdin.readline().rstrip()))

sorted, count = counting_sort(init_list)

# 산술평균 구하기
print(round(sum(sorted)/n))

# 중앙값 구하기
print(sorted[n//2])

# 최빈값 구하기
temp_index = len(count)//2 * -1
max_frequency = max(count)
max_frequency_list = []

for element in count:
    if element != 0 and element >= max_frequency:
        max_frequency_list.append(temp_index)
    temp_index += 1

if len(max_frequency_list) > 1:
    max_frequency_list = counting_sort(max_frequency_list)
    print(max_frequency_list[0][1])
else:
    print(max_frequency_list[0])

# 범위 구하기
print(max(sorted)-min(sorted))