# 최대공약수와 최소공배수
"""
두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.
"""
import sys
A, B = map(int, sys.stdin.readline().rstrip().split())
originA, originB = A, B
r = -1
while r != 0:
    r = A % B
    A, B = B, r
print(A)
print(int(abs(originA*originB)/A))

# A, B = originA, originB
# def getFactors(num):
#     factors = [0 for _ in range(num+1)]
#     i = 2
#     while num > 1:
#         if num % i == 0:
#             num /= i
#             factors[i] += 1
#         else:
#             i += 1
#     return factors
#
# primesA = getFactors(A)
# primesB = getFactors(B)
# A_index = B_index = 2
# a_len = len(primesA)
# b_len = len(primesB)
# LCD = 1
# for i in range(2, max(a_len, b_len)):
#     if i < a_len and i < b_len:
#         temp = max(primesA[i], primesB[i])
#         LCD *= i ** temp
#     elif i >= a_len:
#         LCD *= i ** primesB[i]
#     else:
#         LCD *= i ** primesA[i]
#
# print(LCD)