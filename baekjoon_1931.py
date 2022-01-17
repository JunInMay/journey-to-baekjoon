# 회의실 배정
"""
한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다.
각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자.
단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다.
회의의 시작시간과 끝나는 시간이 같을 수도 있다. 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.
"""
import sys
n = int(sys.stdin.readline().rstrip())

cases = []
for i in range(n):
    cases.append(list(map(int, sys.stdin.readline().rstrip().split())))

def merge(left, right):
    ll = len(left)
    lr = len(right)
    left_index = 0
    right_index = 0
    result = []

    while left_index < ll and right_index < lr:
        if left[left_index][1] < right[right_index][1]:
            result.append(left[left_index])
            left_index += 1

        elif left[left_index][1] == right[right_index][1]:
            if left[left_index][0] <= right[right_index][0]:
                result.append(left[left_index])
                left_index += 1
            else:
                result.append(right[right_index])
                right_index += 1

        else:
            result.append(right[right_index])
            right_index += 1

    while left_index < ll:
        result.append(left[left_index])
        left_index += 1
    while right_index < lr:
        result.append(right[right_index])
        right_index += 1

    return result

def mergesort(li):
    l = len(li)
    if l == 1:
        return li

    left = mergesort(li[:l//2])
    right = mergesort(li[l//2:])
    merged = merge(left, right)

    return merged

sorted_cases = mergesort(cases)
now = 0
count = 0

for case in sorted_cases:
    if now <= case[0]:
        count += 1
        now = case[1]

print(count)