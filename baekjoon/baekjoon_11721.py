# 열 개씩 끊어 출력하기
"""
알파벳 소문자와 대문자로만 이루어진 길이가 N인 단어가 주어진다.
한 줄에 10글자씩 끊어서 출력하는 프로그램을 작성하시오.
"""
import sys

t = sys.stdin.readline().rstrip()
txt = ""
for i in range(len(t)):
    txt += t[i]
    if len(txt) == 10 or i == len(t)-1:
        print(txt)
        txt = ""
