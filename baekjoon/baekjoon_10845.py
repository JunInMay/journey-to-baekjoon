# 큐
"""
정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 여섯 가지이다.

push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
"""
import sys

class myQueue():
    def __init__(self):
        self.queue = []
        self.l = 0
        self.index = 0

    def push(self, elem):
        self.queue.append(elem)
        self.l += 1

    def pop(self):
        if self.l == 0: print(-1)
        else:
            print(self.queue[self.index])
            self.index += 1
            self.l -= 1

    def size(self):
        print(self.l)

    def empty(self):
        if self.l == 0: print(1)
        else: print(0)

    def front(self):
        if self.l == 0: print(-1)
        else:
            print(self.queue[self.index])

    def back(self):
        if self.l == 0: print(-1)
        else:
            print(self.queue[self.index + self.l - 1])

mq = myQueue()
for i in range(int(sys.stdin.readline().rstrip())):
    operand = sys.stdin.readline().rstrip().split()

    if operand[0] == "push":
        mq.push(operand[1])
    elif operand[0] == "pop":
        mq.pop()
    elif operand[0] == "size":
        mq.size()
    elif operand[0] == "empty":
        mq.empty()
    elif operand[0] == "front":
        mq.front()
    elif operand[0] == "back":
        mq.back()