import sys

hour, minute, second = map(int, sys.stdin.readline().rstrip().split())
passed_time = int(sys.stdin.readline().rstrip())
time = hour * 3600 + minute * 60 + second + passed_time

print(time // 3600 % 24, time % 3600 // 60, time % 3600 % 60 % 60)