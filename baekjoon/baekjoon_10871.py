# X보다 작은 수
"""
정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.
"""
import sys
N, X = map(int, sys.stdin.readline().rstrip().split())
init_list = list(map(int, sys.stdin.readline().rstrip().split()))

result = []
for element in init_list:
    if element < X:
        result.append(element)

print(*result)