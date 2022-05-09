import sys

a = 0
b = 0
for n in sys.stdin.readline().rstrip():
    if int(n) == 0:
        if b == 0:
            a = int(str(a) + n)
        else:
            b = int(str(b) + n)
    else:
        if a == 0:
            a = int(n)
        else:
            b = int(n)
print(a + b)