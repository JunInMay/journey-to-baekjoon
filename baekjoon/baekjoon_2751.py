# 수 정렬하기 2
"""
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
합병정렬로 구현했음.
"""

import sys

num = int(sys.stdin.readline().rstrip())

list = []
for i in range(num):
    list.append(int(sys.stdin.readline().rstrip()))

def merge(li1, li2):
    sorted_li = []
    i1 = i2 = 0
    while i1 < len(li1) and i2 < len(li2):
        if li1[i1] <= li2[i2]:
            sorted_li.append(li1[i1])
            i1 += 1
        else:
            sorted_li.append(li2[i2])
            i2 += 1
    while i1 < len(li1):
        sorted_li.append(li1[i1])
        i1 += 1
    while i2 < len(li2):
        sorted_li.append(li2[i2])
        i2 += 1

    return sorted_li

def merge_sort(list):
    if len(list) == 1:
        return list

    half = len(list) // 2
    # left_list = list[:half]
    # right_list = list[half:]
    return merge(merge_sort(list[:half]), merge_sort(list[half:]))

for i in merge_sort(list):
    print(i)