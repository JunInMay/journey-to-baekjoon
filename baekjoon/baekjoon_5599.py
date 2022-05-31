# 카드 정렬
"""
1 から 2n の数が書かれた 2n 枚のカードがあり， 上から 1, 2, 3, ... , 2n の順に積み重なっている．
このカードを， 次の方法を何回か用いて並べ替える．

整数 k でカット
上から k 枚のカードの山 A と 残りのカードの山 B に分けた後， 山 A の上に山 B をのせる．

リフルシャッフル
上から n 枚の山 A と残りの山 B に分け， 上から A の1枚目， B の1枚目， A の2枚目， B の2枚目， …， A の n枚目， B の n枚目， となるようにして， 1 つの山にする．
入力ファイルの指示に従い， カードを並び替えたあとのカードの番号を， 上から順番に出力するプログラムを作成せよ．
"""
"""
문제 대충 번역
1~2n까지 숫자가 적힌 카드가 2n장 있다.
이 카드를 m번 셔플하려고 한다.
셔플 방법은 2가지가 있다.
1~k까지 카드를 밑에 두고, k~2n까지의 카드를 위에 두는 절단 셔플과
1~n부터 n+1~2n까지 카드를 각각 1, n+1, 2, n+2 ... n, 2n 형식으로 한 장씩 끼워넣는 리플 셔플(숏 건 셔플)이 그것이다.
입력으로
첫번째 줄엔 카드 장 수 n(2n이 아님)을 받고,
두번째 줄엔 셔플 횟수 m을 받고,
세번째 줄 부터는 0~2n-1 까지의 숫자가 m줄에 거쳐 들어온다.
0일 경우 리플 셔플, 1 이상일 경우 절단 셔플을 해서 카드가 셔플된 결과를 출력하라.
"""
import sys

cards = [n for n in range(1, int(sys.stdin.readline().rstrip()) * 2 + 1)]


def do_riffle_shuffle(cards):
    result = []
    for i in range(len(cards) // 2):
        result.append(cards[i])
        result.append(cards[i + (len(cards) // 2)])

    return result


for _ in range(int(sys.stdin.readline().rstrip())):
    command = int(sys.stdin.readline().rstrip())

    if command:
        cards = cards[command:] + cards[:command]
    else:
        cards = do_riffle_shuffle(cards)

for card in cards:
    print(card)
