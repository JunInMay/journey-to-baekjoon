# 행복한 소수
"""
Q. : 아래의 수열에서 다음에 올 수를 찾으시오.
313 331 367 ...

경복 : ??
강산 : 379.
경복 : 뭐?
강산 : 행복한 소수잖아.
경복 : 행복한 뭐?
강산 : 그러니까, 자리수의 제곱의 합을 구하는 연산을 계속 반복했을 때 1이 되는 수를 행복한 수라고 하잖아. 행복한 소수는 그 중 소수인 수이고.

7은 분명 소수이다. 과연 행복할까?
7 → 72 = 49
49 → 42 + 92 = 97
97 → 92 + 72 = 130
130 → 12 + 32 + 02 = 10
10 → 12 + 02 = 1
7은 행복한 수이다 ☺.

사실 7은 행복한 소수 중 가장 작은 수이다. (이 문제에서는 1을 소수가 아닌 것으로 생각한다)
어떤 수가 주어지면 이 수가 행복한 소수인지 판정해보자.
"""
import sys

# 정수의 범위
numberRange = 10000

# 자리의 제곱수 구하기
def get_squared_sum(number):
    result = 0
    while number != 0:
        digit = number % 10
        result += digit * digit
        number = number // 10
    return result


# 행복한 수인지 구하기
def dfs(number, visited):
    if number == 1:
        isHappy[number] = True
        return True
    if not visited[number]:
        visited[number] = True
        if dfs(get_squared_sum(number), visited):
            isHappy[number] = True
            return True
    else:
        return False


isHappy = [False for _ in range(get_squared_sum(numberRange-1)+1)]
visited = [False for _ in range(len(isHappy))]
for num in range(len(isHappy)):
    if isHappy[num]:
        continue
    else:
        for i in range(len(visited)):
            visited[i] = False
        dfs(num, visited)


# 소수 여부 구하기
def sieve(primitive):
    for number in range(primitive*2, numberRange+1, primitive):
        isPrimitive[number] = False


isPrimitive = [False, False] + [True for _ in range(numberRange-1)]
for num in range(2, len(isPrimitive)):
    if isPrimitive:
        sieve(num)


for _ in range(int(sys.stdin.readline().rstrip())):
    caseNumber, originalNumber = map(int, sys.stdin.readline().rstrip().split())
    result = "NO"
    if isPrimitive[originalNumber] and isHappy[get_squared_sum(originalNumber)]:
        result = "YES"

    print(f"{caseNumber} {originalNumber} {result}")