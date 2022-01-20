# 단어 정렬
"""
알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

길이가 짧은 것부터
길이가 같으면 사전 순으로
"""
import sys

li = [sys.stdin.readline().rstrip() for _ in range(int(sys.stdin.readline().rstrip()))]

def merge(left, right):
    result = []
    l_index = 0
    r_index = 0
    while l_index < len(left) and r_index < len(right):
        l_elem = left[l_index]
        r_elem = right[r_index]

        if len(l_elem) < len(r_elem):
            result.append(l_elem)
            l_index += 1
        elif len(r_elem) < len(l_elem):
            result.append(r_elem)
            r_index += 1
        else:
            word_len = len(r_elem)
            for i in range(word_len):
                if l_elem[i] < r_elem[i]:
                    result.append(l_elem)
                    l_index += 1
                    break
                elif r_elem[i] < l_elem[i]:
                    result.append(r_elem)
                    r_index += 1
                    break
    while l_index < len(left):
        result.append(left[l_index])
        l_index += 1
    while r_index < len(right):
        result.append(right[r_index])
        r_index += 1
    return result

def merge_sort(lis):
    if len(lis) == 1:
        return lis

    left = merge_sort(lis[:len(lis)//2])
    right = merge_sort(lis[len(lis)//2:])

    return merge(left, right)

sorted_li = merge_sort(list(set(li)))
now = "초기값"
for elem in sorted_li:
    print(elem)