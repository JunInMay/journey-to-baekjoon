# 직사각형으로 나누기
"""
세준이는 N*M크기로 직사각형에 수를 N*M개 써놓았다.

세준이는 이 직사각형을 겹치지 않는 3개의 작은 직사각형으로 나누려고 한다.
각각의 칸은 단 하나의 작은 직사각형에 포함되어야 하고, 각각의 작은 직사각형은 적어도 하나의 숫자를 포함해야 한다.

어떤 작은 직사각형의 합은 그 속에 있는 수의 합이다. 입력으로 주어진 직사각형을 3개의 작은 직사각형으로 나누었을 때,
각각의 작은 직사각형의 합의 곱을 최대로 하는 프로그램을 작성하시오.
"""
import sys
from functools import reduce

# 사각형의 합을 구해서 반환하는 함수
def sum_square(square):
    result = 0
    for i in range(len(square)):
        result += sum(square[i])

    return result

# 한 사각형을 가로로 1회 잘라서 두개로 나누어주는 함수
def slice_square(square, idx):
    first = square[:idx]
    second = square[idx:]

    return first, second


# 사각형을 가로세로를 바꾼 결과를 반환하는 함수 2x8 -> 8x2
def rotate_square(square):
    h = len(square[0]) # 가로
    v = len(square) # 세로
    result = []

    for i in range(h):
        temp = []
        for j in range(v):
            temp.append(square[j][i])
        result.append(temp)

    return result


def get_candidates(square):

    for i in range(1, len(square)):
        res = slice_square(square, i)
        # 여기서 res[1] 에 대해서 len에 대한 제약조건 넣어야 할 수도 있음
        second_square = res[1]
        for j in range(1, len(second_square)):
            second_res1, second_res2 = slice_square(second_square, j)
            candidates.append(reduce(lambda x, y: x * y,[sum_square(res[0]), sum_square(second_res1), sum_square(second_res2)]))

        second_square = rotate_square(second_square)
        for j in range(1, len(second_square)):
            second_res1, second_res2 = slice_square(second_square, j)
            candidates.append(reduce(lambda x, y: x * y,[sum_square(res[0]), sum_square(second_res1), sum_square(second_res2)]))

    for i in range(1, len(square)):
        res = slice_square(square, i)
        # 여기서 res[1] 에 대해서 len에 대한 제약조건 넣어야 할 수도 있음
        second_square = res[0]
        for j in range(1, len(second_square)):
            second_res1, second_res2 = slice_square(second_square, j)
            candidates.append(reduce(lambda x, y: x * y,[sum_square(res[1]), sum_square(second_res1), sum_square(second_res2)]))

        second_square = rotate_square(second_square)
        for j in range(1, len(second_square)):
            second_res1, second_res2 = slice_square(second_square, j)
            candidates.append(reduce(lambda x, y: x * y,[sum_square(res[1]), sum_square(second_res1), sum_square(second_res2)]))


V, H = map(int, sys.stdin.readline().rstrip().split())
square = []
for _ in range(V):
    square.append(list(map(int, list(sys.stdin.readline().rstrip()))))

candidates = []


get_candidates(square)
get_candidates(rotate_square(square))


print(max(candidates))
# 끝나긴 했는데, 리팩토링(아이디어가 있다면) + 코드클리닝을 해보자.


"""
5 3
123
456
789
123
567
"""