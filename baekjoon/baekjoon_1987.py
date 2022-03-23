# 알파벳
"""
세로 R칸, 가로 C칸으로 된 표 모양의 보드가 있다.
보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 좌측 상단 칸 (1행 1열) 에는 말이 놓여 있다.

말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있는데,
새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야 한다.
즉, 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.

좌측 상단에서 시작해서, 말이 최대한 몇 칸을 지날 수 있는지를 구하는 프로그램을 작성하시오.
말이 지나는 칸은 좌측 상단의 칸도 포함된다.
"""
import string
import sys


def dfs(x, y, cnt):
    global result
    result = max(result, cnt)

    for i in range(4):
        nY = y + dy[i]
        nX = x + dx[i]

        if (0 <= nY < R) and (0 <= nX < C) and array[nY][nX] not in visited:
            visited.add(array[nY][nX])
            dfs(nX, nY, cnt+1)
            visited.remove(array[nY][nX])
            # visited[string.ascii_uppercase.index(array[nY][nX])] = False

    return None

# 상하좌우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
R, C = map(int, sys.stdin.readline().rstrip().split())
array = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
# visited = [False for _ in range(len(string.ascii_uppercase))]
# visited[string.ascii_uppercase.index(array[0][0])] = True
visited = set(array[0][0])

result = float('-inf')

dfs(0, 0, 1)
print(result)





