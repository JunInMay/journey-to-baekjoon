# 숫자 야구
"""
정보문화진흥원 정보 영재 동아리에서 동아리 활동을 하던 영수와 민혁이는 쉬는 시간을 틈타 숫자야구 게임을 하기로 했다.

영수는 1에서 9까지의 서로 다른 숫자 세 개로 구성된 세 자리 수를 마음속으로 생각한다. (예: 324)
민혁이는 1에서 9까지의 서로 다른 숫자 세 개로 구성된 세 자리 수를 영수에게 묻는다. (예: 123)
민혁이가 말한 세 자리 수에 있는 숫자들 중 하나가 영수의 세 자리 수의 동일한 자리에 위치하면 스트라이크 한 번으로 센다.
숫자가 영수의 세 자리 수에 있긴 하나 다른 자리에 위치하면 볼 한 번으로 센다.
예) 영수가 324를 갖고 있으면

429는 1 스트라이크 1 볼이다.
241은 0 스트라이크 2 볼이다.
924는 2 스트라이크 0 볼이다.
영수는 민혁이가 말한 수가 몇 스트라이크 몇 볼인지를 답해준다.
민혁이가 영수의 세 자리 수를 정확하게 맞추어 3 스트라이크가 되면 게임이 끝난다.
아니라면 민혁이는 새로운 수를 생각해 다시 영수에게 묻는다.
현재 민혁이와 영수는 게임을 하고 있는 도중에 있다. 민혁이가 영수에게 어떤 수들을 물어보았는지,
그리고 각각의 물음에 영수가 어떤 대답을 했는지가 입력으로 주어진다. 이 입력을 바탕으로 여러분은 영수가 생각하고 있을 가능성이 있는 수가 총 몇 개인지를 알아맞혀야 한다.

아래와 같은 경우를 생각해보자.

민혁: 123
영수: 1 스트라이크 1 볼.
민혁: 356
영수: 1 스트라이크 0 볼.
민혁: 327
영수: 2 스트라이크 0 볼.
민혁: 489
영수: 0 스트라이크 1 볼.
이때 가능한 답은 324와 328, 이렇게 두 가지이다.

영수는 동아리의 규율을 잘 따르는 착한 아이라 민혁이의 물음에 곧이곧대로 정직하게 답한다. 그러므로 영수의 답들에는 모순이 없다.
민혁이의 물음들과 각각의 물음에 대한 영수의 답이 입력으로 주어질 때 영수가 생각하고 있을 가능성이 있는 답의 총 개수를 출력하는 프로그램을 작성하시오.
"""
import sys

questions = []
for _ in range(int(sys.stdin.readline().rstrip())):
    questions.append(tuple(map(int, sys.stdin.readline().rstrip().split())))

candidates = []
for number in range(123, 988):
    hundreds, tens, ones = str(number)

    if hundreds == tens or tens == ones or hundreds == ones:
        continue
    if "0" in str(number):
        continue

    flag = 0
    for question in questions:
        questioned_number, strikes, balls = question
        candidate_strikes = candidate_balls = 0
        for i in range(3):
            for j in range(3):
                if str(number)[i] == str(questioned_number)[j]:
                    if i == j:
                        candidate_strikes += 1
                    else:
                        candidate_balls += 1

        if candidate_strikes != strikes or candidate_balls != balls:
            flag = 1
            break

    if not flag:
        candidates.append(number)

print(len(candidates))