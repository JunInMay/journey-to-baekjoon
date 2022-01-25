# 접미사 배열
"""
접미사 배열은 문자열 S의 모든 접미사를 사전순으로 정렬해 놓은 배열이다.

baekjoon의 접미사는 baekjoon, aekjoon, ekjoon, kjoon, joon, oon, on, n 으로 총 8가지가 있고,
이를 사전순으로 정렬하면, aekjoon, baekjoon, ekjoon, joon, kjoon, n, on, oon이 된다.

문자열 S가 주어졌을 때, 모든 접미사를 사전순으로 정렬한 다음 출력하는 프로그램을 작성하시오.
"""
import sys
txt = sys.stdin.readline().rstrip()
suffixes = []
for i in range(len(txt)):
    suffixes.append(txt[i:])

def merge(left, right):
    result = []
    l = r = 0
    while l < len(left) and r < len(right):
        l_txt = left[l]
        r_txt = right[r]
        min_len = min(len(l_txt), len(r_txt))

        for i in range(min_len):
            if l_txt[i] < r_txt[i]:
                result.append(l_txt)
                l += 1
                break
            elif l_txt[i] > r_txt[i]:
                result.append(r_txt)
                r += 1
                break

    while l < len(left):
        result.append(left[l])
        l += 1
    while r < len(right):
        result.append(right[r])
        r += 1

    return result

def merge_sort(li):
    l = len(li)
    if l <= 1: return li

    left = merge_sort(li[:l//2])
    right = merge_sort(li[l//2:])

    return merge(left, right)

suffixes.sort()
# merge sort 구현했으나 시간초과.

for suffix in suffixes:
    print(suffix)