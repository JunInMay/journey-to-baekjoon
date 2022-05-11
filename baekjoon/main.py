import sys

numbers = []
ab_answers = []


def make_random_integer2(num, a, b):
    return (a * (a * num + b) + b) % 10001


def make_random_integer(num, a, b):
    return (a * num + b) % 10001


N = int(sys.stdin.readline().rstrip())
if N >= 2:
    for _ in range(N):
        numbers.append(int(sys.stdin.readline().rstrip()))
    for a in range(10001):
        if not len(ab_answers):
            for b in range(10001):
                flag = 0
                for i in range(len(numbers) - 1):
                    if make_random_integer2(numbers[i], a, b) != numbers[i + 1]:
                        flag = 1
                if not flag:
                    ab_answers.append((a, b))
                    break
        else:
            break
    for i in range(len(numbers)):
        print(make_random_integer(numbers[i], ab_answers[0][0], ab_answers[0][1]))
else:
    print(0)
"""
1096 1096
"""
