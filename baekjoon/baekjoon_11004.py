# K번째 수
"""
수 N개 A1, A2, ..., AN이 주어진다. A를 오름차순 정렬했을 때, 앞에서부터 K번째 있는 수를 구하는 프로그램을 작성하시오.
"""
import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
array = list(map(int, sys.stdin.readline().rstrip().split()))

def merge(left, right):
    l = r = 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    while l < len(left):
        result.append(left[l])
        l += 1
    while r < len(right):
        result.append(right[r])
        r += 1

    return result

def merge_sort(li):
    n = len(li)
    if n <= 1:
        return li

    left = merge_sort(li[:n//2])
    right = merge_sort(li[n//2:])

    return merge(left, right)

# 머지소트 구현했으나 머지소트로 시간초과가 남. 그냥 내장 정렬 함수 써야겠음.
print(sorted(array)[K-1])


"""
5 2
4 1 2 3 5
"""
