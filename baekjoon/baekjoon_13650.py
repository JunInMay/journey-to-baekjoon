# Botas perdidas
"""
A divisão de Suprimentos de Botas e Calçados do Exército comprou um grande número de pares de botas de vários tamanhos para seus soldados.
No entanto, por uma falha de empacotamento da fábrica contratada, nem todas as caixas entregues continham um par de botas correto,
com duas botas do mesmo tamanho, uma para cada pé. O sargento mandou que os recrutas retirassem todas as botas de todas as caixas para reembalá-las,
desta vez corretamente.

Quando o sargento descobriu que você sabia programar,
ele solicitou com a gentileza habitual que você escrevesse um programa que, dada a lista contendo a descrição de cada bota entregue,
determina quantos pares corretos de botas poderão ser formados no total.
"""
"""
문제 대충 번역
신병들한테 신발을 엄청 보급해줬는데 모든 신발들이 사이즈가 맞질 않는다.
예를 들어 신병 A한테 보급한 270 사이즈 신발이 오른쪽은 270, 왼쪽은 265 이런 식이다.
그래서 신발을 모두 꺼내어 짝이 되는 신발은 몇 켤레인지 세고자 한다.
주의할 점은 EOF 처리를 해야 한다. 따로 반복문의 종료는 언급되지 않는다.
"""
import sys

while True:
    try:
        boots = [[0, 0] for _ in range(60-30+1)]
        result = 0
        for _ in range(int(sys.stdin.readline().rstrip())):
            size, side = sys.stdin.readline().rstrip().split()
            if side == "D":
                boots[int(size)-30][1] += 1
            elif side == "E":
                boots[int(size)-30][0] += 1
        for boot in boots:
            result += min(boot)
        print(result)
    except:
        break
