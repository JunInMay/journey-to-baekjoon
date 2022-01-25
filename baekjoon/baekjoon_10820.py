# 문자열 분석
"""
문자열 N개가 주어진다. 이때, 문자열에 포함되어 있는 소문자, 대문자, 숫자, 공백의 개수를 구하는 프로그램을 작성하시오.
각 문자열은 알파벳 소문자, 대문자, 숫자, 공백으로만 이루어져 있다.
"""
import sys

cases = []
while True:
    txt = sys.stdin.readline()
    txt = txt[:len(txt)-1]
    if len(txt) == 0: break
    cases.append(txt)

for case in cases:
    counts = [0, 0, 0, 0]
    for t in case:
        tt = ord(t)
        if tt >= 97 and tt <= 122:
            counts[0] += 1
        elif tt >= 65 and tt <= 90:
            counts[1] += 1
        elif tt >= 48 and tt <= 57:
            counts[2] += 1
        elif tt == 32:
            counts[3] += 1
    print(*counts)