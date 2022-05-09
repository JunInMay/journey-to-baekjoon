# 접두사
"""
접두사X 집합이란 집합의 어떤 한 단어가, 다른 단어의 접두어가 되지 않는 집합이다.
예를 들어, {hello}, {hello, goodbye, giant, hi}, 비어있는 집합은 모두 접두사X 집합이다.
하지만, {hello, hell}, {giant, gig, g}는 접두사X 집합이 아니다.

단어 N개로 이루어진 집합이 주어질 때, 접두사X 집합인 부분집합의 최대 크기를 출력하시오.
"""
import sys

input_words = []
for _ in range(int(sys.stdin.readline().rstrip())):
    input_words.append(sys.stdin.readline().rstrip())

input_words.sort(key=lambda x : len(x), reverse=True)

prefixX = []
for i in range(len(input_words)):
    for j in range(i, len(input_words)):
        if len(input_words[i]) > len(input_words[j]):
            continue
        else:
            if input_words[i] == input_words[j]:
                continue

    flag = 0
    for j in range(len(prefixX)):
        if prefixX[j][:len(input_words[i])] == input_words[i]:
            flag = 1
            break

    if not flag:
        prefixX.append(input_words[i])
print(len(prefixX))

"""
4
prefix
prefix
pref
p
"""