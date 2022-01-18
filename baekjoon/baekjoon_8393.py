# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.
n = int(input())

if n % 2 == 0:
    result = (n+1)*(n/2)
else:
    result = (n+1)*(n//2) + (n+1)/2
print(int(result))