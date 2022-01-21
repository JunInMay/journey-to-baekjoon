# 별 찍기 - 16
"""
예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.
"""
import sys
n = int(sys.stdin.readline().rstrip())

for i in range(n):
    flag = 0
    txt = " "*(n-(i+1))
    for j in range((i+1)*2-1):
        if flag == 0:
            txt += "*"
            flag = 1
        else:
            txt += " "
            flag = 0

    print(txt)
