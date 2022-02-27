# 별 찍기 - 11
"""
예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.
"""
import sys


def make_star(n):
    if n == 3:
        return ["*", "* *", "*****"]
    else:
        top_triangle = []
        bottom_triangle = []
        next_triangle = make_star(n//2)

        for line in next_triangle:
            top_triangle.append(line)

        level = n-1
        for i in range(len(next_triangle)):
            bottom_triangle.append(next_triangle[i])
            bottom_triangle[i] += " " * level
            level -= 2
            bottom_triangle[i] += next_triangle[i]

        return top_triangle + bottom_triangle


def print_star(n):
    star = make_star(n)

    for i in range(len(star)):
        space = " " * (n-i-1)
        print(space + star[i] + space)


print_star(int(sys.stdin.readline().rstrip()))