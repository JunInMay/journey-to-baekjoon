import sys

A, B = map(int, sys.stdin.readline().rstrip().split())
quotient, remainder = A//B , A%B

if remainder < 0:
    quotient += 1
    remainder -= B

print(quotient)
print(remainder)