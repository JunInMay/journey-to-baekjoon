# 팩토리얼 0의 개수
"""
N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.
"""
import sys



N = int(sys.stdin.readline().rstrip())
# 1안(통과, 문제에서 의도한 바는 아님)
# N이 2464일 때 까지밖에 계산해주지 못했음.
# sys.setrecursionlimit(1000000)
# factorial = [1, 1]
#
# def get_factorial(n):
#     l = len(factorial)
#     if n < l:
#         return factorial[n]
#
#     factorial.append(n*get_factorial(n-1))
#
#     return factorial[n]
#
# num = get_factorial(N)
# res = 0
# for c in str(num)[::-1]:
#     if c == "0":
#         res += 1
#     else: break
# print(res)


# 2안, 팩토리얼 값에 0이 들어가는 경우를 수학적으로 따짐
# N이 1천조이어도 빠르게 결과가 나옴.
quotient = N
res = 0
while quotient > 4:
    quotient //= 5
    res += quotient
print(res)