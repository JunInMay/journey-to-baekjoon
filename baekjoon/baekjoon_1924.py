# 2007년
"""
오늘은 2007년 1월 1일 월요일이다. 그렇다면 2007년 x월 y일은 무슨 요일일까? 이를 알아내는 프로그램을 작성하시오.
"""
import sys
m, d = map(int, sys.stdin.readline().rstrip().split())
correction = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
days = {
    0: "MON",
    1: "TUE",
    2: "WED",
    3: "THU",
    4: "FRI",
    5: "SAT",
    6: "SUN"
}
print(days[(sum(correction[:m-1])+(d-1))%7])
