# 덱
"""
정수를 저장하는 덱(Deque)를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 여덟 가지이다.

push_front X: 정수 X를 덱의 앞에 넣는다.
push_back X: 정수 X를 덱의 뒤에 넣는다.
pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 덱에 들어있는 정수의 개수를 출력한다.
empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
"""
import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class myDeQue():
    def __init__(self):
        self.first = None
        self.last = None
        self.l = 0

    def push_front(self, elem):
        node = Node(elem)
        if self.l == 0:
            self.first = node
            self.last = node
        else:
            self.first.prev = node
            node.next = self.first
            self.first = node
        self.l += 1
    def push_back(self, elem):
        node = Node(elem)
        if self.l == 0:
            self.first = node
            self.last = node
        else:
            node.prev = self.last
            self.last.next = node
            self.last = node
        self.l += 1

    def pop_front(self):
        if self.l == 0:
            print(-1)
        else:
            print(self.first.data)
            temp = self.first.next
            self.first.next = None
            self.first = temp
            self.l -= 1

    def pop_back(self):
        if self.l == 0:
            print(-1)
        else:
            print(self.last.data)
            temp = self.last.prev
            self.last.prev = None
            self.last = temp
            self.l -= 1

    def size(self):
        print(self.l)

    def empty(self):
        if self.l == 0: print(1)
        else: print(0)

    def front(self):
        if self.l == 0: print(-1)
        else: print(self.first.data)

    def back(self):
        if self.l == 0: print(-1)
        else: print(self.last.data)

mdq = myDeQue()
for i in range(int(sys.stdin.readline().rstrip())):
    operation = sys.stdin.readline().rstrip().split()
    if operation[0] == "push_front":
        mdq.push_front(int(operation[1]))
    elif operation[0] == "push_back":
        mdq.push_back(int(operation[1]))
    elif operation[0] == "pop_front":
        mdq.pop_front()
    elif operation[0] == "pop_back":
        mdq.pop_back()
    elif operation[0] == "size":
        mdq.size()
    elif operation[0] == "empty":
        mdq.empty()
    elif operation[0] == "front":
        mdq.front()
    elif operation[0] == "back":
        mdq.back()
