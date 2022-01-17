# 체스판 다시 칠하기
"""
지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 MxN 크기의 보드를 찾았다.
어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다.
지민이는 이 보드를 잘라서 8x8 크기의 체스판으로 만들려고 한다.
체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다. 구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고,
변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다.
따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다. 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.
보드가 체스판처럼 칠해져 있다는 보장이 없어서, 지민이는 8x8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다.
당연히 8*8 크기는 아무데서나 골라도 된다. 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.
"""
import sys

# 하얀색(W)이 인자로 오면 B(검은색)를 반환하고, 반대면 W를 반환하는 함수(체스판의 다음 색을 결정해주기 위해)
def switch_color(color):
    if color == 'W':
        return 'B'
    else:
        return 'W'

# 주어진 체스판의 왼쪽 위가 W, B로 각각 칠해지는 케이스에 따라서 가장 덜 칠하는 케이스가 무엇인지 반환하는 함수
def verify_board(board):
    # 체스판의 왼쪽 위를 W로 하여 칠하는 케이스
    white = coloring(board, 'W')
    # 체스판의 왼쪽 위를 B로 하여 칠하는 케이스
    black = coloring(board, 'B')

    return min(white, black)

# 체스판의 왼쪽 위를 무엇으로 칠할 것인가(start)에 따라서 주어진 체스판이 얼마나 잘못 칠해져있는지 개수를 반환하는 함수
def coloring(board, start):
    count = 0
    vertical_wb = start
    for row in board:
        horizontal_wb = vertical_wb
        for col in row:
            if col != horizontal_wb:
                count += 1
            horizontal_wb = switch_color(horizontal_wb)
        vertical_wb = switch_color(vertical_wb)

    return count

count_rows, count_cols = map(int, sys.stdin.readline().rstrip().split())
original_board = []

for i in range(count_rows):
    row = list(sys.stdin.readline().rstrip())
    original_board.append(row)

results = []
for row in range(count_rows-7):
    for col in range(count_cols-7):
        temp = []
        for i in range(8):
            temp.append(original_board[row+i][col:col+8])
        results.append(verify_board(temp))

print(min(results))