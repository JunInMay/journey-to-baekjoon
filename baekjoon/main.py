import string
import sys

result = 0
for _ in range(int(sys.stdin.readline().rstrip())):
    check = [False for _ in range(26)]
    count = 1
    before = ""
    for char in sys.stdin.readline().rstrip():
        i = string.ascii_lowercase.index(char)
        if before == "":
            check[i] = True
            before = char
        if before != char:
            if not check[i]:
                check[i] = True
                before = char
            else:
                count = 0
                break
    result += count

print(result)
