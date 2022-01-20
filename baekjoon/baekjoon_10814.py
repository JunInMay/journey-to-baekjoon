# 나이순 정렬
"""
온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다.
이때, 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오.
"""
import sys

members = []
for i in range(int(sys.stdin.readline().rstrip())):
    age, name = sys.stdin.readline().rstrip().split()
    members.append((int(age), name, i))

def merge(left, right):
    result = []
    l_index = r_index = 0
    while l_index < len(left) and r_index < len(right):
        if left[l_index][0] == right[r_index][0]:
            if left[l_index][2] < right[r_index][2]:
                result.append(left[l_index])
                l_index += 1
            else:
                result.append(right[r_index])
                r_index += 1
        elif left[l_index][0] < right[r_index][0]:
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

def merge_sort(li):
    if len(li) == 1:
        return li

    left = merge_sort(li[:len(li)//2])
    right = merge_sort(li[len(li)//2:])

    return merge(left, right)

for mem in merge_sort(members):
    print(mem[0], mem[1])