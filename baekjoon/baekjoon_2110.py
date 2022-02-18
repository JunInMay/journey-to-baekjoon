# 공유기 설치
"""
도현이의 집 N개가 수직선 위에 있다. 각각의 집의 좌표는 x1, ..., xN이고,
집 여러개가 같은 좌표를 가지는 일은 없다.

도현이는 언제 어디서나 와이파이를 즐기기 위해서 집에 공유기 C개를 설치하려고 한다.
최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에, 한 집에는 공유기를 하나만 설치할 수 있고,
가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.

C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하시오.
"""
import sys

N, C = map(int, sys.stdin.readline().rstrip().split())
houses = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
houses.sort()

floor = 0
ceil = houses[N-1] - floor

while floor <= ceil:
    mid = (ceil + floor) // 2
    start = float('-inf')
    cnt = 0
    for house in houses:
        if house - start >= mid:
            cnt += 1
            start = house
    if cnt >= C:
        floor = mid + 1
    else:
        ceil = mid - 1
print(ceil)

"""
3 2
1
3
7

4 3
11
13
16
18
ans : 2
output : 10
"""