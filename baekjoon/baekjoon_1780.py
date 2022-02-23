# 종이의 개수
"""
N×N크기의 행렬로 표현되는 종이가 있다. 종이의 각 칸에는 -1, 0, 1 중 하나가 저장되어 있다.
우리는 이 행렬을 다음과 같은 규칙에 따라 적절한 크기로 자르려고 한다.

만약 종이가 모두 같은 수로 되어 있다면 이 종이를 그대로 사용한다.
(1)이 아닌 경우에는 종이를 같은 크기의 종이 9개로 자르고, 각각의 잘린 종이에 대해서 (1)의 과정을 반복한다.
이와 같이 종이를 잘랐을 때, -1로만 채워진 종이의 개수,
0으로만 채워진 종이의 개수, 1로만 채워진 종이의 개수를 구해내는 프로그램을 작성하시오.
"""
# def print_paper(paper):
#     for line in paper:
#         print(*line)
#     return None
import sys

paper = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(int(sys.stdin.readline().rstrip()))]


def check_paper(paper):
    checker = paper[0][0]
    result = checker
    if checker == -1:
        cand1 = 0
        cand2 = 1
    elif checker == 0:
        cand1 = -1
        cand2 = 1
    else:
        cand1 = -1
        cand2 = 0

    for line in paper:
        if cand1 in line or cand2 in line:
            result = "No"
            break
    return result

def cut_paper(paper):
    c = check_paper(paper)
    if c != "No":
        result[c+1] += 1
    else:
        size = len(paper[0])
        for level in range(3):
            rect1, rect2, rect3 = [[], [], []]
            for i in range(size//3):
                rect1.append(paper[level*(size//3) + i][:size // 3])
                rect2.append(paper[level*(size//3) + i][size // 3:(size // 3)*2])
                rect3.append(paper[level*(size//3) + i][(size // 3)*2:])
            cut_paper(rect1)
            cut_paper(rect2)
            cut_paper(rect3)

    return None

result = [0, 0, 0]
cut_paper(paper)
for line in result:
    print(line)
