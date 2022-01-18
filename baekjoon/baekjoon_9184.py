# 신나는 함수 실행
"""
재귀 호출만 생각하면 신이 난다! 아닌가요?
다음과 같은 재귀함수 w(a, b, c)가 있다.

if a <= 0 or b <= 0 or c <= 0, then w(a, b, c) returns:
    1

if a > 20 or b > 20 or c > 20, then w(a, b, c) returns:
    w(20, 20, 20)

if a < b and b < c, then w(a, b, c) returns:
    w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

otherwise it returns:
    w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

위의 함수를 구현하는 것은 매우 쉽다. 하지만, 그대로 구현하면 값을 구하는데 매우 오랜 시간이 걸린다. (예를 들면, a=15, b=15, c=15)
a, b, c가 주어졌을 때, w(a, b, c)를 출력하는 프로그램을 작성하시오.
"""
"""
파이썬의 리스트, shallow copy와 deep copy에 대해서 고민하고 풀어야 한다...
문제의 주제와 다르긴 하지만.
"""
import sys

input = []
cases = []
while input != [-1, -1, -1]:
    input = list(map(int, sys.stdin.readline().rstrip().split()))
    if input != [-1, -1, -1]:
        cases.append(input)

memo = []
for i in range(51):
    row = []
    for j in range(51):
        col = []
        for k in range(51):
            col.append("")
        row.append(col)
    memo.append(row)

def w(a, b, c):
    global memo

    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        if memo[20][20][20] != "":
            return memo[20][20][20]
        else:
            return w(20, 20, 20)

    if memo[a][b][c] == "":
        if a < b and b < c:
            A = w(a, b, c-1)
            B = w(a, b-1, c-1)
            C = w(a, b-1, c)

            memo[a][b][c] = A+B-C
        else:
            A = w(a-1, b, c)
            B = w(a-1, b-1, c)
            C = w(a-1, b, c-1)
            D = w(a-1, b-1, c-1)

            memo[a][b][c] = A+B+C-D

    return memo[a][b][c]

for case in cases:
    result = w(case[0], case[1], case[2])
    print(f"w({case[0]}, {case[1]}, {case[2]}) = {result}")