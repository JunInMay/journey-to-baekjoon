# 병든 나이트
"""
병든 나이트가 N × M 크기 체스판의 가장 왼쪽아래 칸에 위치해 있다.
병든 나이트는 건강한 보통 체스의 나이트와 다르게 4가지로만 움직일 수 있다.

2칸 위로, 1칸 오른쪽
1칸 위로, 2칸 오른쪽
1칸 아래로, 2칸 오른쪽
2칸 아래로, 1칸 오른쪽
병든 나이트는 여행을 시작하려고 하고, 여행을 하면서 방문한 칸의 수를 최대로 하려고 한다.
병든 나이트의 이동 횟수가 4번보다 적지 않다면, 이동 방법을 모두 한 번씩 사용해야 한다.
이동 횟수가 4번보다 적은 경우(방문한 칸이 5개 미만)에는 이동 방법에 대한 제약이 없다.

체스판의 크기가 주어졌을 때, 병든 나이트가 여행에서 방문할 수 있는 칸의 최대 개수를 구해보자.
"""
import sys

V, H = map(int, sys.stdin.readline().rstrip().split())

def get_visit(V, H):

    cnt = 1
    H -= 1
    # 세로가 1칸(어떠한 움직임도 불가능함)
    if V <= 1:
        return cnt
    # 세로가 2칸(2, 3번 움직임만 가능 = 최대 이동 횟수는 3회임)
    elif V <= 2:
        order = 2
        for i in range(3):
            H -= order
            cnt += 1
            if H < 0:
                cnt -= 1
                break
    # 세로가 3칸 이상
    else:
        # 가로가 부족할 경우 1, 4번 움직임만, 최대 이동 횟수는 3회
        if H <= 5:
            order = 1
            for i in range(3):
                H -= order
                cnt += 1
                if H < 0:
                    cnt -= 1
                    break
        else:
            cnt += (H-4) + 2
        
    return cnt


print(get_visit(V, H))