# 충돌의 수
"""
길이가 $L$인 상자가 있다. 이 안에 크기를 무시할 수 있을 만큼 작은 공 $N$개가 존재한다.
길이가 $L$인 상자는 길이가 $1$인 구간 $L$개로 분할할 수 있으며, 모든 공은 구간과 구간 사이의 경계에서 운동을 시작한다.
모든 공들은 $1$초에 한 칸씩 움직인다. 만약 어떤 공이 벽이나 다른 공에 충돌한다면, 즉시 운동 방향이 반대로 바뀐다.
이때 공의 속력은 바뀌지 않는다. 또한 처음에 임의의 두 공 사이 간격은 짝수이고, 한 위치엔 하나의 공만 존재한다.

예를 들어, 위 그림은 $L=8$일 때를 나타낸 것이다.
시간 $t=0$일 때 빨간색 공은 처음 위치 $1$에서 오른쪽으로 이동하고 있고, 파란 공은 처음 위치 $5$에서 왼쪽으로 운동하고 있다.
$t=2$일 때 두 공은 충돌하여 즉시 운동 방향이 반대로 바뀌게 된다.

 $N$개의 공들의 처음 위치와 처음 운동 방향이 주어질 때, 시간 $T$초까지 공끼리 몇 번 충돌하는지 구하는 프로그램을 작성하시오.
"""
import sys

L, N, T = map(int, sys.stdin.readline().rstrip().split())
balls = []

for _ in range(N):
    location, direction = sys.stdin.readline().rstrip().split()
    balls.append([int(location), direction])

def convert_direction(direction):
    if direction == "L":
        return "R"
    else:
        return "L"

result = 0
for _ in range(T):
    # 공 움직임
    for ball in balls:
        if ball[1] == "L":
            ball[0] -= 1
        else:
            ball[0] += 1
    balls.sort(key=lambda x: x[0])
    # 벽 충돌 확인
    for ball in balls:
        if ball[0] == 0:
            ball[1] = convert_direction(ball[1])
        elif ball[0] == L:
            ball[1] = convert_direction(ball[1])
    # 공 충돌 확인
    for i in range(len(balls)-1):
        if balls[i][0] == balls[i+1][0]:
            balls[i][1] = convert_direction(balls[i][1])
            balls[i+1][1] = convert_direction(balls[i+1][1])
            result += 1
print(result)

"""
4 2 5
1 R
3 L

8 2 18
1 R
5 L
"""