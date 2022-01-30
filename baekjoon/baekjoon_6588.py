# 골드바흐의 추측
"""
1742년, 독일의 아마추어 수학가 크리스티안 골드바흐는 레온하르트 오일러에게 다음과 같은 추측을 제안하는 편지를 보냈다.

4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있다.
예를 들어 8은 3 + 5로 나타낼 수 있고, 3과 5는 모두 홀수인 소수이다.
또, 20 = 3 + 17 = 7 + 13, 42 = 5 + 37 = 11 + 31 = 13 + 29 = 19 + 23 이다.

이 추측은 아직도 해결되지 않은 문제이다.
백만 이하의 모든 짝수에 대해서, 이 추측을 검증하는 프로그램을 작성하시오.
"""
import sys

input_num = -1

# 솟수 판별이 필요하다는 것을 깨달았으므로, 처음부터 sieve를 쓰기로 결정
sieve = [True for _ in range(999998)]
sieve[0:1] = [False, False]

for i in range(len(sieve)):
    if sieve[i]:
        for j in range(i*2, len(sieve), i):
            sieve[j] = False

while input_num != 0:
    input_num = int(sys.stdin.readline().rstrip())

    flag = 1
    for lvl in range(3, int(input_num/2)+1):
        # 소수인지 아닌지 알아내야 한다.
        if sieve[lvl] and sieve[input_num-lvl]:
            print(f"{input_num} = {lvl} + {input_num-lvl}")
            flag = 0
            break

    if flag and input_num != 0:
        print("Goldbach's conjecture is wrong.")