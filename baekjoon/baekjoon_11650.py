# 좌표 정렬하기
"""
2차원 평면 위의 점 N개가 주어진다.
좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.
"""
import sys
n = int(sys.stdin.readline().rstrip())

coordinates = []
for i in range(n):
    coordinates.append(list(map(int, sys.stdin.readline().rstrip().split())))
def merge(left, right):
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index][0] < right[right_index][0]:
            result.append(left[left_index])
            left_index += 1

        elif right[right_index][0] < left[left_index][0]:
            result.append(right[right_index])
            right_index += 1

        else:
            if left[left_index][1] <= right[right_index][1]:
                result.append(left[left_index])
                left_index += 1
            else:
                result.append(right[right_index])
                right_index += 1

    while left_index < len(left):
        result.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        result.append(right[right_index])
        right_index += 1

    return result

def mergesort(coordinates):
    if len(coordinates) == 1:
        return coordinates

    left = mergesort(coordinates[:len(coordinates)//2])
    right = mergesort(coordinates[len(coordinates)//2:])

    return merge(left, right)

coordinates = mergesort(coordinates)

for coordinate in coordinates:
    print(*coordinate)