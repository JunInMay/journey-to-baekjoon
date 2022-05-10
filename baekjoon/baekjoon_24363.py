# ПРАВОЪГЪЛНИЦИ
"""
Ванко разрязал правоъгълен лист хартия на три правоъгълни части, след което ги разхвърлил из стаята.
Брат му Петьо се прибрал и се опитал да подреди частите отново в цял правоъгълник със същата площ като тази на нарязания.
Напишете програма rect, която да подскаже на Петьо как да го направи.
"""
"""
실패 : 원인 규명되지 않음
"""
import sys

rectangles = []
for _ in range(3):
    rectangles.append(list(map(int, sys.stdin.readline().rstrip().split())))

is_series = False

for i in range(2):
    if rectangles[0][i] in rectangles[1] and rectangles[0][i] in rectangles[2]:
        is_series = True

common_column = 0
common_row = 0
if is_series:
    common_column = rectangles[0][i]
    for i in range(3):
        if rectangles[i][0] != common_column:
            rectangles[i][0], rectangles[i][1] = rectangles[i][1], rectangles[i][0]

    body = []
    for i in range(3):
        body.append(".")
        for _ in range(rectangles[i][1] - 1):
            body.append(" ")
    body.append(".")

    cap = ["." for _ in range(sum((rectangles[0][1], rectangles[1][1], rectangles[2][1])) + 1)]
    for i in range(common_column + 1):
        if i != 0 and i != common_column:
            print(*body)
        else:
            print(*cap)

else:
    i = 0
    flag = 0
    while not flag:
        if i != 2:
            j = i + 1
        else:
            j = 0

        for k in range(2):
            if not flag:
                for l in range(2):
                    if rectangles[i][k] + rectangles[j][l] in rectangles[3-(i+j)]:
                        if rectangles[i][1-k] == rectangles[j][1-l]:
                            common_row = rectangles[i][1 - k]
                            common_column = rectangles[i][k] + rectangles[j][l]
                            rectangles = [rectangles[i], rectangles[j], rectangles[3-(i+j)]]
                            flag = 1
                            break
        i += 1

    # A, B 좌우 교환
    for i in range(2):
        if rectangles[i][0] != common_row:
            rectangles[i][0], rectangles[i][1] = rectangles[i][1], rectangles[i][0]

    # A, B 상하 교환
    if rectangles[0][1] > rectangles[1][1]:
        rectangles[0], rectangles[1] = rectangles[1], rectangles[0]

    # C 좌우 교환
    if rectangles[2][0] != common_column:
        rectangles[2][0], rectangles[2][1] = rectangles[2][1], rectangles[2][0]

    for i in range(common_column + 1):
        cap = ["." for _ in range(rectangles[2][1] + common_row + 1)]
        if i == 0 or i == common_column:
            print(*cap)
        else:
            line = ["."]
            if i == rectangles[0][1]:
                for _ in range(common_row):
                    line.append(".")
            else:
                for _ in range(common_row-1):
                    line.append(" ")
                line.append(".")
            for _ in range(rectangles[2][1] - 1):
                line.append(" ")
            line.append(".")
            print(*line)

"""
5 5
5 5
10 10
"""