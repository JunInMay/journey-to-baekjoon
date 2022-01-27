# 진법 변환 2
"""
10진법 수 N이 주어진다. 이 수를 B진법으로 바꿔 출력하는 프로그램을 작성하시오.
10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다.
이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.

A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35
"""
import sys

result = []
A, B = map(int, sys.stdin.readline().rstrip().split())

while A > 0:
    if A >= B:
        r = A % B
        A = (A-r) / B
        char = int(r)
    else:
        char = int(A)
        A -= A
    if char >= 10:
        char = chr((char-10)+65)
    result.append(str(char))
print("".join(result[::-1]))

