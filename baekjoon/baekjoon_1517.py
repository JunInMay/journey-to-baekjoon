# 버블 소트
"""
N개의 수로 이루어진 수열 A[1], A[2], …, A[N]이 있다.
이 수열에 대해서 버블 소트를 수행할 때, Swap이 총 몇 번 발생하는지 알아내는 프로그램을 작성하시오.

버블 소트는 서로 인접해 있는 두 수를 바꿔가며 정렬하는 방법이다.
예를 들어 수열이 3 2 1 이었다고 하자. 이 경우에는 인접해 있는 3, 2가 바뀌어야 하므로 2 3 1 이 된다.
다음으로는 3, 1이 바뀌어야 하므로 2 1 3 이 된다. 다음에는 2, 1이 바뀌어야 하므로 1 2 3 이 된다.
그러면 더 이상 바꿔야 할 경우가 없으므로 정렬이 완료된다.
"""
import sys
cnt = 0


def merge(left, right):
    global cnt
    result = []
    l_index = 0
    r_index = 0
    while l_index < len(left) and r_index < len(right):
        if left[l_index] <= right[r_index]:
            result.append(left[l_index])
            l_index += 1
        else:
            result.append(right[r_index])
            r_index += 1
            cnt += (len(left) - l_index)

    while l_index < len(left):
        result.append(left[l_index])
        l_index += 1
    while r_index < len(right):
        result.append(right[r_index])
        r_index += 1

    return result


def merge_sort(li):
    n = len(li)
    if n <= 1:
        return li
    left = merge_sort(li[:n//2])
    right = merge_sort(li[n//2:])

    return merge(left, right)


N = int(sys.stdin.readline().rstrip())
l = list(map(int, sys.stdin.readline().rstrip().split()))

merge_sort(l)
print(cnt)