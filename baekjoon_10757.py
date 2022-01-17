# 큰 수 A+B
"""
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 A와 B가 주어진다. (0 < A,B < 10^10000)
"""
import sys
A, B = sys.stdin.readline().rstrip().split()

max_len = len(A) if len(A) >= len(B) else len(B)
if len(A) < len(B):
    A = (max_len-len(A)) * "0" + A
else:
    B = (max_len-len(B)) * "0" + B

result = ""
carry = 0
for i in range(max_len):
    sum_num = int(A[-(i+1)]) + int(B[-(i+1)]) + carry
    carry = 1 if sum_num >= 10 else 0
    result += str(sum_num-carry*10)

if carry != 0:
    result+=str(carry)
print(result[::-1])