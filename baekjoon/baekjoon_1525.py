# 퍼즐
"""
3×3 표에 다음과 같이 수가 채워져 있다. 오른쪽 아래 가장 끝 칸은 비어 있는 칸이다.

1	2	3
4	5	6
7	8
어떤 수와 인접해 있는 네 개의 칸 중에 하나가 비어 있으면, 수를 그 칸으로 이동시킬 수가 있다.
물론 표 바깥으로 나가는 경우는 불가능하다. 우리의 목표는 초기 상태가 주어졌을 때, 최소의 이동으로 위와 같은 정리된 상태를 만드는 것이다. 다음의 예를 보자.

1	 	3
4	2	5
7	8	6

1	2	3
4	 	5
7	8	6

1	2	3
4	5
7	8	6

1	2	3
4	5	6
7	8
가장 윗 상태에서 세 번의 이동을 통해 정리된 상태를 만들 수 있다. 이와 같이 최소 이동 횟수를 구하는 프로그램을 작성하시오.
"""
import sys
from collections import deque

# 배열크기
l = 3
# 상하좌우
dC = [-l, l, -1, 1]


def bfs(start):
    queue = deque([(start, start.index("0"), 0)])

    while queue:
        # 다음 배열, 인덱스, 비용
        arr, idx, count = queue.popleft()
        if arr == correctArray:
            return count
        for i in range(4):
            # 다음 인덱스
            nIdx = idx + dC[i]
            if i >= 2 and idx // 3 != nIdx // 3:
                continue
            elif nIdx < 0 or nIdx > l*l-1:
                continue

            # 다음 배열
            nArr = list(arr)
            nArr[idx], nArr[nIdx] = nArr[nIdx], nArr[idx]
            nArr = "".join(nArr)

            # 이미 확인한 배열이라면 continue
            if not capturedArrays.get(nArr):
                capturedArrays[nArr] = True
                queue.append((nArr, nArr.index("0"), count+1))
    return -1

# 입력 배열
array = ""
for _ in range(l):
    array += "".join(list(sys.stdin.readline().rstrip().split()))


# 정답 배열(1 2 3 4 5 6 7 8 0)
correctArray = "".join([str(n) for n in range(1, 9)] + ["0"])
# 확인한 배열 저장
capturedArrays = {}
print(bfs(str(array)))

"""
1 2 3
4 5 6
7 0 8
"""