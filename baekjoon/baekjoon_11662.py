# 민호와 강호
"""
민호와 강호가 2차원 좌표 평면 위에 있다. 민호는 점 A(Ax, Ay)에서 점 B(Bx, By)를 향해 걸어가고 있고,
강호는 점 C(Cx, Cy)에서 점 D(Dx, Dy)를 향해 걸어가고 있다. 민호와 강호는 동시에 출발하고,
민호가 점 B에 도착하는 순간 강호도 점 D에 도착한다. 또, 두 사람은 항상 일정한 속도로 걸어간다.
두 사람의 거리가 가장 가까울 때, 거리를 구하는 프로그램을 작성하시오.

두 점 (x1, y1), (x2, y2)사이의 거리는 \(\sqrt{(x2-x1)^2 + (y2-y1)^2}\) 이다.
"""
"""
삼분탐색(Ternary Search)을 통해 푸는 문제.
삼분탐색은 peak가 있는 실수 정의역에서 활용할 수 있는 알고리즘이다.
"""
import sys, math

def get_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    y = y2-y1
    x = x2-x1

    return math.sqrt(x*x + y*y)

def apply(point1, point2, proportion):
    x1, y1 = point1
    x2, y2 = point2
    return ((x2-x1)*proportion+x1, (y2-y1)*proportion+y1)


inputs = list(map(int, sys.stdin.readline().rstrip().split()))
A, B, C, D = [(inputs[i*2], inputs[i*2+1]) for i in range(4)]

error = 10**-10 # 혹시 모르니 오차 10^-10으로 세팅..

floor = 0
ceil = 1

while (ceil - floor) > error:
    mid1 = (floor * 2 + ceil) / 3
    mid2 = (floor + ceil * 2) / 3
    res1 = get_distance(apply(A, B, mid1), apply(C, D, mid1))
    res2 = get_distance(apply(A, B, mid2), apply(C, D, mid2))

    if res1 >= res2:
        floor = mid1 + error
    elif res1 < res2:
        ceil = mid2 - error
    else:
        floor = mid1 + error
        ceil = mid2 - error
print('%.10f' % res2)

"""
0 0 5 5 10 7 5 5
"""