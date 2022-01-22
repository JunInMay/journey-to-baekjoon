# 가장 긴 바이토닉 부분 수열
"""
수열 S가 어떤 수 Sk를 기준으로 S1 < S2 < ... Sk-1 < Sk > Sk+1 > ... SN-1 > SN을 만족한다면, 그 수열을 바이토닉 수열이라고 한다.
예를 들어, {10, 20, 30, 25, 20}과 {10, 20, 30, 40}, {50, 40, 25, 10} 은 바이토닉 수열이지만,
{1, 2, 3, 2, 1, 2, 3, 2, 1}과 {10, 20, 30, 40, 20, 30} 은 바이토닉 수열이 아니다.

수열 A가 주어졌을 때, 그 수열의 부분 수열 중 바이토닉 수열이면서 가장 긴 수열의 길이를 구하는 프로그램을 작성하시오.
"""
import sys
n = int(sys.stdin.readline().rstrip())
sequence = list(map(int, sys.stdin.readline().rstrip().split()))

from_left_memo = [0 for _ in range(n)]
from_right_memo = [0 for _ in range(n)]
bitonics = [0 for _ in range(n)]
# left / right
for i in range(1, n):
    for j in range(i):
        if sequence[i-(j+1)] < sequence[i]:
            from_left_memo[i] = max(from_left_memo[i-(j+1)]+1, from_left_memo[i])
        if sequence[n-i+j] < sequence[n-i-1]:
            from_right_memo[n-i-1] = max(from_right_memo[n-i+j]+1, from_right_memo[n-i-1])
for i in range(n):
    bitonics[i] = from_left_memo[i] + from_right_memo[i] + 1
print(max(bitonics))