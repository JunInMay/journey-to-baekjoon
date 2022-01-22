# 1, 2, 3 더하기
"""
정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.

1+1+1+1
1+1+2
1+2+1
2+1+1
2+2
1+3
3+1
"""
import sys
memo = [0, 1, 2, 4]
for _ in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip())
    if n >= len(memo):
        for i in range(len(memo), n+1):
            memo.append(memo[i-3]+memo[i-2]+memo[i-1])
    print(memo[n])