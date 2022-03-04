# 수 묶기
"""
길이가 N인 수열이 주어졌을 때, 그 수열의 합을 구하려고 한다.
하지만, 그냥 그 수열의 합을 모두 더해서 구하는 것이 아니라, 수열의 두 수를 묶으려고 한다.
어떤 수를 묶으려고 할 때, 위치에 상관없이 묶을 수 있다. 하지만, 같은 위치에 있는 수(자기 자신)를 묶는 것은 불가능하다.
그리고 어떤 수를 묶게 되면, 수열의 합을 구할 때 묶은 수는 서로 곱한 후에 더한다.

예를 들면, 어떤 수열이 {0, 1, 2, 4, 3, 5}일 때, 그냥 이 수열의 합을 구하면 0+1+2+4+3+5 = 15이다.
하지만, 2와 3을 묶고, 4와 5를 묶게 되면, 0+1+(2*3)+(4*5) = 27이 되어 최대가 된다.

수열의 모든 수는 단 한번만 묶거나, 아니면 묶지 않아야한다.
수열이 주어졌을 때, 수열의 각 수를 적절히 묶었을 때, 그 합이 최대가 되게 하는 프로그램을 작성하시오.
"""
"""
1. 음수끼리는 무조건 곱해야 한다.
2. 0은 양수와 곱하면 안된다. 0을 곱한다면 '홀로남은' 절대값이 제일 작은 음수와 곱해야 한다.
3. 양수는 1과 곱하면 안된다. 1을 그냥 더하면 된다.
"""
import sys

negatives = []
positives = []
isThereZero = 1  # 0이 하나라도 들어오면 0, 없으면 1
for i in range(int(sys.stdin.readline().rstrip())):
    value = int(sys.stdin.readline().rstrip())

    if value > 0:
        positives.append(value)
    elif value < 0:
        negatives.append(value)
    else:
        isThereZero = 0

result = 0

negatives.sort(key=lambda x : abs(x), reverse=True)
for i in range(0, len(negatives), 2):
    if i+1 < len(negatives):
        result += negatives[i] * negatives[i+1]
    else:
        if isThereZero == 0:
            result += negatives[i] * isThereZero
        else:
            result += negatives[i]

positives.sort(reverse=True)
for i in range(0, len(positives), 2):
    if i+1 < len(positives):
        if positives[i] == 1 or positives[i+1] == 1:
            result += positives[i] + positives[i+1]
        else:
            result += positives[i] * positives[i+1]
    else:
        result += positives[i]

print(result)

"""
5
-4
-2
-5
-1
-10

4
-4
-2
-5
-10
"""