# 수 찾기
"""
N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
"""
import sys

N = int(sys.stdin.readline().rstrip())
numbers = sorted(list(map(int, sys.stdin.readline().rstrip().split())))

def binary_search(num):
    bottom = 0
    top = len(numbers)-1

    while bottom <= top:
        mid = (bottom + top)//2
        if numbers[mid] < num:
            bottom = mid + 1
        elif numbers[mid] > num:
            top = mid - 1
        elif numbers[mid] == num:
            return 1
    return 0

M = int(sys.stdin.readline().rstrip())
for num in list(map(int, sys.stdin.readline().rstrip().split())):
    print(binary_search(num))