import sys

N = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().rstrip().split()))
m = max(sequence)

r_sequence = list(map(lambda x: x/m*100, [x for x in sequence]))

print(sum(r_sequence)/len(r_sequence))