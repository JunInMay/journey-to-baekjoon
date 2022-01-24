# 국영수
"""
도현이네 반 학생 N명의 이름과 국어, 영어, 수학 점수가 주어진다. 이때, 다음과 같은 조건으로 학생의 성적을 정렬하는 프로그램을 작성하시오.

국어 점수가 감소하는 순서로
국어 점수가 같으면 영어 점수가 증가하는 순서로
국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로 (단, 아스키 코드에서 대문자는 소문자보다 작으므로 사전순으로 앞에 온다.)
"""
import sys

li = [sys.stdin.readline().rstrip().split() for _ in range(int(sys.stdin.readline().rstrip()))]
for elem in li:
    for i in range(4):
        if i >= 1:
            elem[i] = int(elem[i])

def merge(left, right):
    l = 0
    r = 0
    result = []
    while l < len(left) and r < len(right):
        if left[l][1] > right[r][1]:
            result.append(left[l])
            l += 1
        elif left[l][1] < right[r][1]:
            result.append(right[r])
            r += 1
        else:
            if left[l][2] < right[r][2]:
                result.append(left[l])
                l += 1
            elif left[l][2] > right[r][2]:
                result.append(right[r])
                r += 1
            else:
                if left[l][3] > right[r][3]:
                    result.append(left[l])
                    l += 1
                elif left[l][3] < right[r][3]:
                    result.append(right[r])
                    r += 1
                else:
                    min_len = min(len(left[l][0]), len(right[r][0]))
                    flag = 0
                    for i in range(min_len):
                        if left[l][0][i] < right[r][0][i]:
                            result.append(left[l])
                            l += 1
                            flag = 1
                            break
                        elif left[l][0][i] > right[r][0][i]:
                            result.append(right[r])
                            r += 1
                            flag = 1
                            break

                    # 이름을 다 쟀는데도 똑같으면 길이가 짧은 사람을 넣자. (문제 조건엔 없지만..)
                    # 길이조차 똑같으면 그냥 오른쪽 사람을 넣음(그냥 동일한 데이터나 진배없으므로)
                    if flag == 0:
                        if len(left[l][0]) < len(right[r][0]):
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

merge_sorted = merge_sort(li)
for case in merge_sorted:
    print(case[0])

"""
11
Junkyu 10 10 10
Sangkeun 10 10 10
Sunyoung 10 10 10
Soong 10 10 10
Haebin 10 10 10
Kangsoo 10 10 10
Donghyuk 10 10 10
Sei 10 10 10
Wonseob 10 10 10
Sanghyun 10 10 10
nsj 10 10 10
"""