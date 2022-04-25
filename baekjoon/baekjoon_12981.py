# 공 포장하기
"""
빨간 공 R개, 초록 공 G개, 파란 공 B개를 가지고 있다.
오늘은 이 공을 박스로 포장하려고 한다. 박스에는 공이 1개, 2개, 또는 3개 들어갈 수 있다.
박스에 들어가는 공의 색은 모두 다르거나, 모두 같아야 한다.
필요한 박스 개수의 최솟값을 구하는 프로그램을 작성하시오.
"""
import sys

R, G, B = map(int, sys.stdin.readline().rstrip().split())

count = 0

count += R // 3
count += G // 3
count += B // 3
R %= 3
G %= 3
B %= 3

m = min([R, G, B])
count += m
R -= m
G -= m
B -= m

if R >= 2:
    count += R // 2
    R %= 2
if G >= 2:
    count += G // 2
    G %= 2
if B >= 2:
    count += B // 2
    B %= 2

if not R and G and B:
    m = min(G, B)
    count += m
    G -= m
    B -= m
elif R and not G and B:
    m = min(R, B)
    count += m
    R -= m
    B -= m
elif R and G and not B:
    m = min(R, G)
    count += m
    R -= m
    G -= m

count += R
count += G
count += B

print(count)