# 큐 2
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
        self.qsize = 0
        self.index = 0

    def push(self, elem):
        self.queue.append(elem)
        self.qsize += 1

    def pop(self):
        if self.qsize == 0:
            print(-1)
        else:
            print(self.queue[self.index])
            self.index += 1
            self.qsize -= 1

    def size(self):
        print(self.qsize)

    def empty(self):
        if self.qsize == 0:
            print(1)
        else:
            print(0)

    def front(self):
        if self.qsize == 0:
            print(-1)
        else:
            print(self.queue[self.index])

    def back(self):
        if self.qsize == 0:
            print(-1)
        else:
            print(self.queue[self.index+self.qsize-1])

q = myQueue()
for i in range(int(sys.stdin.readline().rstrip())):
    input = sys.stdin.readline().rstrip().split()
    if input[0] != 'push':
        operand = input[0]
    else:
        operand = input[0]
        elem = input[1]
    if operand == 'push':
        q.push(elem)
    elif operand == 'front':
        q.front()
    elif operand == 'back':
        q.back()
    elif operand == 'pop':
        q.pop()
    elif operand == 'size':
        q.size()
    elif operand == 'empty':
        q.empty()