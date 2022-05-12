# Diplomatic License
"""
In an effort to minimize the expenses for foreign affairs the countries of the world have argued as follows.
It is not enough that each country maintains diplomatic relations with at most one other country, for then,
since there are more than two countries in the world, some countries cannot communicate with each other through (a chain of) diplomats.

Now, let us assume that each country maintains diplomatic relations with at most two other countries.
It is an unwritten diplomatic "must be" issue that every country is treated in an equal fashion.
It follows that each country maintains diplomatic relations with exactly two other countries.

International topologists have proposed a structure that fits these needs.
They will arrange the countries to form a circle and let each country have diplomatic relations with its left and right neighbours.
In the real world, the Foreign Office is located in every country's capital.
For simplicity, let us assume that its location is given as a point in a two-dimensional plane. If you connect the Foreign Offices of the diplomatically related countries by a straight line, the result is a polygon.

It is now necessary to establish locations for bilateral diplomatic meetings.
Again, for diplomatic reasons, it is necessary that both diplomats will have to travel equal distances to the location.
For efficiency reasons, the travel distance should be minimized. Get ready for your task!
"""
"""
- 주저리주저리 말이 많지만 대충 번역 -
나라가 여러 개 있다. 나라 별로 수도가 하나 씩 있다.
여러 케이스가 있고, 각각의 케이스별로 나라의 개수 N과 첫번째 나라의 수도부터 N(N>=3, 홀수)번째 나라의 수도까지 좌표쌍 x, y로 하여 입력으로 주어진다.
3 3 3 4 4 5 5 이런 식이다. 이러면 나라가 3개고, 각 수도의 좌표는 각각 (3, 3), (4, 4), (5, 5)이다.
나라는 입력된 순서대로 인접해있다고 가정하고, 인접한 두 나라끼리 외교 미팅을 해야 한다.
외교 미팅은 각 나라에서 동일하게 떨어진 거리에서 이뤄진다.
첫 번째로 입력된 나라와 마지막으로 입력된 나라는 인접해있다고 가정한다.
외교 미팅의 개수와 외교 미팅이 일어나는 좌표 x, y들을 각각 출력하라.
"""
"""
해설
인접한 나라의 수도를 잇는 선분의 중점의 좌표를 출력하면 된다.
"""
import sys


def get_midpoint(point_a, point_b):
    return (point_a[0] + point_b[0]) / 2, (point_a[1] + point_b[1]) / 2


while True:
    try:
        input_numbers = list(map(int, sys.stdin.readline().rstrip().split()))
        N = input_numbers[0]
        coordinates = [(input_numbers[i], input_numbers[i + 1]) for i in range(1, len(input_numbers), 2)]
        midpoints = []
        answer = []
        for i in range(-1, -(len(coordinates) + 1), -1):
            midpoint = get_midpoint(coordinates[i], coordinates[i + 1])
            answer.append(midpoint[1])
            answer.append(midpoint[0])
        answer.append(N)
        answer = answer[::-1]
        print(answer[0], end="")
        for i in range(1, len(answer), 2):
            print(f" {answer[i]:.6f} {answer[i + 1]:.6f}", end="")
        print()
    except:
        break
