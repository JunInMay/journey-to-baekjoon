# 스택
"""
정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 다섯 가지이다.

push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
"""
import sys

class myStack():
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack = [element] + self.stack

    def pop(self):
        if len(self.stack) >= 1:
            element = self.stack[0]
            self.stack = self.stack[1:]
            return element
        else:
            return -1

    def size(self):
        return len(self.stack)

    def empty(self):
        if len(self.stack) == 0:
            return 1
        else: return 0

    def top(self):
        if self.empty():
            return -1
        else:
            return self.stack[0]

n = int(sys.stdin.readline().rstrip())
ms = myStack()
commands = []
for i in range(n):
    text = sys.stdin.readline().rstrip().split()
    commands.append(text)

for command in commands:
    if command[0] == "push":
        ms.push(int(command[1]))
    elif command[0] == "top":
        print(ms.top())
    elif command[0] == "size":
        print(ms.size())
    elif command[0] == "pop":
        print(ms.pop())
    elif command[0] == "empty":
        print(ms.empty())