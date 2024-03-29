# 요세푸스 문제
"""
요세푸스 문제는 다음과 같다.

1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다.
이제 순서대로 K번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다.
이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다.
예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.

N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.
"""
"""
항상 자료구조 문제가 나오면 자료구조를 구현하고
정렬 문제가 나오면 정렬을 구현했는데
그냥 의미가 없다. 어차피 구현해도 느리다고 틀린다.
그냥 내장 자료구조를 쓰는게 낫지않을까.
이번에도 큐 구현했다가 느리대서 그냥 deque import 해서 썼다. 빠르더라.
근데 내가 deque를 몰라서 안쓰는 것도 아니고 알아도 그냥 구현해서 내 스스로 푸는게 보람차다고 생각했기 때문에 안쓰는 것인데,
적당히 문제에서 요구하는대로 로지컬하기만 하면 맞다고 통과해 줄 정도로 시간을 주는게 합당하다고 생각한다.
그렇지만? 절대 그렇게 해주지 않을 것이므로 어떠한 경우든 파이썬 같이 느려터진 언어로 문제를 풀 생각이라면
배열 혹은 그 비슷한 것들을 이용할 때 무조건 deque를 써야한다고 가슴 깊이 새기고 되도록이면 빠르게 파이썬에서 손을 떼야겠다.
"""
import sys

class Node():
    def __init__(self, elem):
        self.data = elem
        self.prev = None
        self.next = None

class MyQueue():
    def __init__(self):
        self.first = None
        self.last = None
        self.l = 0

    def push(self, elem):
        node = Node(elem)
        if self.l == 0:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            node.prev = self.last
            self.last = node
        self.l += 1

    def pop(self):
        if self.l >= 1:
            if self.l >= 2:
                temp = self.first.next
                result = self.first.data
                self.first.next = None
                self.first = temp
                self.first.prev = None
            else:
                result = self.first.data
                self.first = None
                self.last = None
            self.l -= 1
        else: return None
        return result
import sys
from collections import deque

N, K = map(int, sys.stdin.readline().rstrip().split())
deq = deque([_ for _ in range(1, N+1)])

result = []
# 빠른코드
for _ in range(N):
    deq.rotate(-(K-1))
    result.append(deq.popleft())

# 느려터진코드
# for _ in range(N):
#     for i in range(K-1):
#         deq.append(deq.popleft())
#     result.append(deq.popleft())

print("<"+", ".join(map(str, result))+">")