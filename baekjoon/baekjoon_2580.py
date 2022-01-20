# 스도쿠
"""
스도쿠는 18세기 스위스 수학자가 만든 '라틴 사각형'이랑 퍼즐에서 유래한 것으로 현재 많은 인기를 누리고 있다.
이 게임은 아래 그림과 같이 가로, 세로 각각 9개씩 총 81개의 작은 칸으로 이루어진 정사각형 판 위에서 이뤄지는데,
게임 시작 전 일부 칸에는 1부터 9까지의 숫자 중 하나가 쓰여 있다.

나머지 빈 칸을 채우는 방식은 다음과 같다.

각각의 가로줄과 세로줄에는 1부터 9까지의 숫자가 한 번씩만 나타나야 한다.
굵은 선으로 구분되어 있는 3x3 정사각형 안에도 1부터 9까지의 숫자가 한 번씩만 나타나야 한다.
위의 예의 경우, 첫째 줄에는 1을 제외한 나머지 2부터 9까지의 숫자들이 이미 나타나 있으므로 첫째 줄 빈칸에는 1이 들어가야 한다.

또한 위쪽 가운데 위치한 3x3 정사각형의 경우에는 3을 제외한 나머지 숫자들이 이미 쓰여있으므로 가운데 빈 칸에는 3이 들어가야 한다.

이와 같이 빈 칸을 차례로 채워 가면 다음과 같은 최종 결과를 얻을 수 있다.

게임 시작 전 스도쿠 판에 쓰여 있는 숫자들의 정보가 주어질 때 모든 빈 칸이 채워진 최종 모습을 출력하는 프로그램을 작성하시오.
"""
"""
pypy로 제출
배운거1 : return 하면 재귀 1스택만 backward로 갈 뿐 프로그램은 반복된다.(0으로 가득찬 input 제출시 여러개의 답을 제출하게 됨)
배운거2 : exit(0) 프로그램 종료
배운거3 : 백트래킹 기본 테크닉. 값변경 > 재귀 호출(1단계 더 deep하게) > 값복구 하면 괜히 deepcopy로 시복 올리지 않고 해결 가능.
"""
import sys
sudoku = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(9)]

def isAlright(y, x, li):
    next_y = y+1 if x == 8 else y
    next_x = x+1 if x < 8 else 0

    if next_y == 9 and next_x == 1:
        for s in li:
            print(*s)
        exit(0)

    if li[y][x] != 0:
        isAlright(next_y, next_x, li)
    else:
        horizontal_filter = li[y]
        vertical_filter = list(map(lambda f: f[x], li))
        square_filter = sum(list(map(lambda l: l[(x // 3) * 3:(x // 3 + 1) * 3], li[(y // 3) * 3:(y // 3 + 1) * 3])), [])
        for i in range(1, 10):
            # 가로 검열
            cri1 = False
            if i not in horizontal_filter:
                cri1 = True

            # 세로 검열
            cri2 = False
            if i not in vertical_filter:
                cri2 = True

            # 정사각형 검열
            cri3 = False
            if i not in square_filter:
                cri3 = True

            if cri1 and cri2 and cri3:
                li[y][x] = i
                isAlright(next_y, next_x, li)
                li[y][x] = 0

isAlright(0, 0, sudoku)

"""
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
"""