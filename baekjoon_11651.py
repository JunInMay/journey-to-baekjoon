# 좌표 정렬하기 2
"""
2차원 평면 위의 점 N개가 주어진다.
좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.
"""
import sys
n = int(sys.stdin.readline().rstrip())

coordinates = []
for _ in range(n):
    coordinate = list(map(int, sys.stdin.readline().rstrip().split()))
    coordinates.append(coordinate)

def merge(left, right):
    l_index = 0
    r_index = 0
    result = []

    while l_index < len(left) and r_index < len(right):
        if left[l_index][1] == right[r_index][1]:
            if left[l_index][0] < right[r_index][0]:
                result.append(left[l_index])
                l_index += 1
            else:
                result.append(right[r_index])
                r_index += 1
        elif left[l_index][1] < right[r_index][1]:
            result.append(left[l_index])
            l_index += 1
        else:
            result.append(right[r_index])
            r_index += 1

    while l_index < len(left):
        result.append(left[l_index])
        l_index += 1
    while r_index < len(right):
        result.append(right[r_index])
        r_index += 1
    return result

def mergeSort(li):
    if len(li) == 1:
        return li
    l = len(li)
    left = mergeSort(li[:l//2])
    right = mergeSort(li[l//2:])

    return merge(left, right)

merged = mergeSort(coordinates)
for coordinate in merged:
    print(*coordinate)