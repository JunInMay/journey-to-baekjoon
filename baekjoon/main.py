import sys

number = (int(sys.stdin.readline().rstrip()) + int(sys.stdin.readline().rstrip())) % 12
print(number if number != 0 else 12)
