# 최소, 최대
"""
N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
"""
import sys
n = int(sys.stdin.readline().rstrip())
li = list(map(int, sys.stdin.readline().rstrip().split()))
print(min(li), max(li))