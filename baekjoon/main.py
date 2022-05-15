import sys
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
print(abs(numbers[1] - numbers[0]))