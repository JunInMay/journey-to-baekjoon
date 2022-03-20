# 암호 만들기
"""
바로 어제 최백준 조교가 방 열쇠를 주머니에 넣은 채 깜빡하고 서울로 가 버리는 황당한 상황에 직면한 조교들은,
702호에 새로운 보안 시스템을 설치하기로 하였다. 이 보안 시스템은 열쇠가 아닌 암호로 동작하게 되어 있는 시스템이다.

암호는 서로 다른 L개의 알파벳 소문자들로 구성되며 최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성되어 있다고 알려져 있다.
또한 정렬된 문자열을 선호하는 조교들의 성향으로 미루어 보아 암호를 이루는 알파벳이 암호에서 증가하는 순서로 배열되었을 것이라고 추측된다.
즉, abc는 가능성이 있는 암호이지만 bac는 그렇지 않다.

새 보안 시스템에서 조교들이 암호로 사용했을 법한 문자의 종류는 C가지가 있다고 한다. 이 알파벳을 입수한 민식,
영식 형제는 조교들의 방에 침투하기 위해 암호를 추측해 보려고 한다. C개의 문자들이 모두 주어졌을 때, 가능성 있는 암호들을 모두 구하는 프로그램을 작성하시오.
"""
import sys
from collections import deque


def isVowel(char):
    if char in vowels:
        return True

    return False


def bfs(start):
    vow = 1 if start in vowels else 0
    con = 1 if start in consonants else 0
    queue = deque([(start, vow, con, len(start))])
    while queue:
        password, vow, con, size = queue.popleft()
        last = password[size - 1]
        if size == L:
            print(password)
            continue

        for i in range(characters_input.index(last) + 1, C - (L - size) + 1):
            # 앞으로 더 받을 수 있는 문자의 길이
            left = L - size

            nVow, nCon = graph[i]

            if vow + nVow < 1:
                continue
            if con + nCon < 2:
                continue

            
            if isVowel(characters_input[i]):
                # 받으려 하는 문자가 모음일 경우 자음이 들어갈 자리가 충분한지 검사
                if left - 1 >= 2 - con:
                    queue.append((password + characters_input[i], vow + 1, con, size + 1))
                else:
                    continue
            else:
                if left - 1 >= 1 - vow:
                    queue.append((password + characters_input[i], vow, con+1, size + 1))
                else:
                    continue

    return None


L, C = map(int, sys.stdin.readline().rstrip().split())
characters_input = sorted(sys.stdin.readline().rstrip().split())
vowels = []
consonants = []

for char in characters_input:
    if char in ['a', 'e', 'i', 'o', 'u']:
        vowels.append(char)
    else:
        consonants.append(char)

l_vow = len(vowels)
l_con = len(consonants)
# 각 인덱스별 남은 vow/cos의 개수를 저장하는 리스트
graph = []
for i in range(C):
    graph.append((l_vow, l_con))
    if isVowel(characters_input[i]):
        l_vow -= 1
    else:
        l_con -= 1

result = []
for i in range(C):
    if i <= C - L:
        bfs(characters_input[i])

"""
15 15
a b c d e f g h i j k l m n o         

3 5
a e z b w      -> abe가 왜나옴?     
"""
