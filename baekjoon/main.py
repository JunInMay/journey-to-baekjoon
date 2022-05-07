import sys

N = int(sys.stdin.readline().rstrip())

for i in range(N):
    print(" " * i + "*" * ((2*N)-(1+(2 * i))))


from datetime import datetime
now = datetime.now()
print(now.year)
print(f"{now.month:02d}")
print(f"{now.day:02d}")