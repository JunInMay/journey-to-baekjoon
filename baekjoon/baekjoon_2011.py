# 암호코드
"""
상근이와 선영이가 다른 사람들이 남매간의 대화를 듣는 것을 방지하기 위해서 대화를 서로 암호화 하기로 했다. 그래서 다음과 같은 대화를 했다.

상근: 그냥 간단히 암호화 하자. A를 1이라고 하고, B는 2로, 그리고 Z는 26으로 하는거야.
선영: 그럼 안돼. 만약, "BEAN"을 암호화하면 25114가 나오는데, 이걸 다시 글자로 바꾸는 방법은 여러 가지가 있어.
상근: 그렇네. 25114를 다시 영어로 바꾸면, "BEAAD", "YAAD", "YAN", "YKD", "BEKD", "BEAN" 총 6가지가 나오는데, BEAN이 맞는 단어라는건 쉽게 알수 있잖아?
선영: 예가 적절하지 않았네 ㅠㅠ 만약 내가 500자리 글자를 암호화 했다고 해봐. 그 때는 나올 수 있는 해석이 정말 많은데, 그걸 언제 다해봐?
상근: 얼마나 많은데?
선영: 구해보자!
어떤 암호가 주어졌을 때, 그 암호의 해석이 몇 가지가 나올 수 있는지 구하는 프로그램을 작성하시오.
"""
import string
import sys
alphabet = [-1] + list(string.ascii_uppercase)
password = sys.stdin.readline().rstrip()

if len(password) == 0 : print(0)
elif int(password[0]) == 0 : print(0)
else:
    memo = [1, 1]
    for i in range(1, len(password)):
        over_ten = int(password[i-1:i+1])
        temp = 0
        if over_ten >= 10 and over_ten <= 26:
            temp += memo[i-1]
        elif int(password[i]) == 0:
            print("0")
            exit(0)
        if int(password[i]) != 0:
            temp += memo[i]
        memo.append(temp%1000000)
    print(memo[len(memo)-1])
