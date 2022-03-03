# 30
"""
어느 날, 미르코는 우연히 길거리에서 양수 N을 보았다.
미르코는 30이란 수를 존경하기 때문에, 그는 길거리에서 찾은 수에 포함된 숫자들을 섞어 30의 배수가 되는 가장 큰 수를 만들고 싶어한다.

미르코를 도와 그가 만들고 싶어하는 수를 계산하는 프로그램을 작성하라.
"""
"""
Tip. 세상엔 배수 판별법이라는 것이 존재한다. 이걸 이 문제를 풀면서 깨달았다.
"""
import sys

n = sys.stdin.readline().rstrip()
if "0" in n:
    if (sum(map(int, n))%3 == 0):
        print("".join(sorted(n, reverse=True)))
        exit()
print(-1)


