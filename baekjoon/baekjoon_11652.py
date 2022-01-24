# 카드
"""
준규는 숫자 카드 N장을 가지고 있다. 숫자 카드에는 정수가 하나 적혀있는데,
적혀있는 수는 -262보다 크거나 같고, 262보다 작거나 같다.

준규가 가지고 있는 카드가 주어졌을 때, 가장 많이 가지고 있는 정수를 구하는 프로그램을 작성하시오.
만약, 가장 많이 가지고 있는 정수가 여러 가지라면, 작은 것을 출력한다.
"""
import sys

cards = []
for i in range(int(sys.stdin.readline().rstrip())):
    cards.append(int(sys.stdin.readline().rstrip()))

def merge(left, right):
    l = 0
    r = 0
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
    if len(li) <= 1:
        return li
    left = merge_sort(li[:len(li)//2])
    right = merge_sort(li[len(li)//2:])

    return merge(left, right)

cards = merge_sort(cards)

info = [0, cards[0]]
candidates = []
max_count = float('-inf')
for i in range(len(cards)):
    number = cards[i]
    if info[1] != number:
        candidates.append(info[:])
        info[0] = 1
        info[1] = number
    else:
        info[0] += 1
        max_count = max(max_count, info[0])
candidates.append(info)

for c in candidates:
    if c[0] == max_count:
        print(c[1])
        break