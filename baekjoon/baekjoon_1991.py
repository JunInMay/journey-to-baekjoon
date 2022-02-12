# 트리 순회
"""
이진 트리를 입력받아 전위 순회(preorder traversal), 중위 순회(inorder traversal), 후위 순회(postorder traversal)한 결과를 출력하는 프로그램을 작성하시오.

예를 들어 위와 같은 이진 트리가 입력되면,

전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)
가 된다.
"""
import sys

class node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = None
        self.right = None

        if left != ".":
            self.left = left
        if right != ".":
            self.right = right

tree = {}
for _ in range(int(sys.stdin.readline().rstrip())):
    data, left, right = sys.stdin.readline().rstrip().split()
    tree[data] = node(data, left, right)

def preorder(n):
    result = ""
    result = n.data
    if n.left != None:
        result += preorder(tree[n.left])
    if n.right != None:
        result += preorder(tree[n.right])

    return result

def inorder(n):
    result = ""
    if n.left != None:
        result += inorder(tree[n.left])
    result += n.data
    if n.right != None:
        result += inorder(tree[n.right])

    return result

def postorder(n):
    result = ""
    if n.left != None:
        result += postorder(tree[n.left])
    if n.right != None:
        result += postorder(tree[n.right])
    result += n.data

    return result

print(preorder(tree['A']))
print(inorder(tree['A']))
print(postorder(tree['A']))