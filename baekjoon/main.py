import sys

sequence = [int(sys.stdin.readline().rstrip()) for _ in range(10)]
result = set()
for i in range(len(sequence)):
    result.add(sequence[i] % 42)
print(len(result))
