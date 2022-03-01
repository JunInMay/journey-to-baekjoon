# 가장 가까운 두 점
"""
2차원 평면상에 n개의 점이 주어졌을 때, 이 점들 중 가장 가까운 두 점을 구하는 프로그램을 작성하시오.
"""
"""
실패, 분할정복으로 풀어볼 것
"""
import sys

coordinates = sorted([tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(int(sys.stdin.readline().rstrip()))])

def get_distance(p1, p2):
    x = p2[0] - p1[0]
    y = p2[1] - p1[1]
    return y*y + x*x

start = ""
end = ""
dist = float("inf")
candidates = []
for i in range(len(coordinates)):
    if start == "":
        start = coordinates[i]
    elif end == "":
        end = coordinates[i]
        dist = get_distance(start, end)
    else:
        fromStart = get_distance(start, coordinates[i])
        fromEnd = get_distance(end, coordinates[i])
        if fromStart >= dist and fromEnd >= dist:
            candidates.append(dist)
            start = coordinates[i]
            end = ""
        else:
            if fromStart < fromEnd:
                end = coordinates[i]
                dist = fromStart
            else:
                start = end
                end = coordinates[i]
                dist = fromEnd
candidates.append(dist)
print(min(candidates))

"""
4
0 0
0 4
2 2
2 3
"""