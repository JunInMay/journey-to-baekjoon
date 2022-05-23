# 감소하는 수
"""
음이 아닌 정수 X의 자릿수가 가장 큰 자릿수부터 작은 자릿수까지 감소한다면, 그 수를 감소하는 수라고 한다.
예를 들어, 321과 950은 감소하는 수지만, 322와 958은 아니다. N번째 감소하는 수를 출력하는 프로그램을 작성하시오. 0은 0번째 감소하는 수이고,
1은 1번째 감소하는 수이다. 만약 N번째 감소하는 수가 없다면 -1을 출력한다.
"""
import sys

declining_numbers = []
N = int(sys.stdin.readline().rstrip())

before_numbers = [number for number in range(10)]
digit_count = 0
while digit_count < 10:
    temp = []
    for i in range(len(before_numbers)):
        for candidate in range(int(str(before_numbers[i])[0]) + 1, 10):
            temp.append(int(str(candidate) + str(before_numbers[i])))
    temp.sort()
    declining_numbers += before_numbers
    before_numbers = temp
    digit_count += 1

try:
    print(declining_numbers[N])
except IndexError:
    print(-1)

