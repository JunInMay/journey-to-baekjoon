# Mountains Beyond Mountains
"""
만리장성, 에펠 탑, 그리고 부르즈 할리파까지!
동서고금을 막론하고 세계의 유명 건축물의 건설에는 항상 Constructor’s High 사(이하 CH 주식회사)가 함께했다.
건축계의 최고 전문가들인 그들은, 최근 건설한 거대 고속도로의 모습을 대중들에게 홍보하기 위해 준비 중이다.

CH 주식회사의 직원 범수는, 고속도로의 모습이 담긴 큰 그림을 그리는 임무를 맡았다.
범수는 N × M 픽셀의 디지털 이미지로 큰 그림을 그리게 될 것이며, 큰 그림에는 큰 산맥과, 그 사이를 시원하게 가로지르는 크고 아름다운 고속도로의 모습이 그려지게 될 것이다.

범수는, ‘.’ (ASCII Code 46) 으로 차 있는 빈 이미지 파일에 큰 그림을 그리려고 한다.
범수가 현재 전달받은 정보는 산의 고도 정보와, 고속도로의 높이이다.

산의 고도 정보는 M개의 음이 아닌 정수 H1, H2, · · · , HM으로 주어지며, 왼쪽에서 i번째 픽셀은, 땅에서부터 Hi의 높이만큼 산이 영역을 차지하는 형태로 그려져야 한다.
산은, ‘#’ (ASCII Code 35) 문자로 출력되어야 한다.

고속도로는 높이 X(아래에서 X번째 픽셀)의 가로줄을 차지하게 될 것이다.
고속도로가 지나는 세로줄의 산의 높이가 X 이상이면, 고속도로는 터널의 형태로 건설되며, ‘*’ (ASCII Code 42) 문자로 출력되어야 한다.
고속도로가 지나는 세로줄의 산의 높이가 X 미만이면, 고속도로는 다리의 형태로 건설되며, ‘-’ (ASCII Code 45) 문자로 출력되어야 한다.

한편, 왼쪽에서 i번째 픽셀에 다리를 건설할 때, i가 3의 배수라면, 해당 지점에 교각을 건설해야 한다.
교각은 높이가 X − 1인 지점부터 산 바로 위까지를 잇게 되며, ‘|’ (ASCII Code 124) 문자로 출력되어야 한다.

범수는 어제 큰 그림을 멋지게 완성하고 뿌듯한 마음으로 퇴근했지만,
애석하게도 악당 재현이가 범수의 컴퓨터를 열어서 큰 그림을 휴지통에 넣고 비워버렸다.
범수가 회사에 와서 이 사실을 알게 되면 큰 슬픔에 빠질 것이 분명하니, 여러분이 범수 대신 큰 그림을 그려주자.
"""
import sys

N, M, X = map(int, sys.stdin.readline().rstrip().split())
mountains = list(map(int, sys.stdin.readline().rstrip().split()))

picture = [[chr(46) for _ in range(M)] if h != N-X else [chr(45) for _ in range(M)] for h in range(N)]

for i in range(M):
    for h in range(max(mountains[i], X-1)):
        point = -(h+1)
        if h < mountains[i]:
            if picture[point][i] == chr(46):
                picture[point][i] = chr(35)
            elif picture[point][i] == chr(45):
                picture[point][i] = chr(42)
        else:
            if i % 3 == 2:
                picture[point][i] = chr(124)

for line in picture:
    print(*line)

"""
8 10 5
1 4 2 3 7 3 2 5 3 0
8 10 5
8 8 8 8 8 8 8 8 8 8
8 10 5
5 5 5 5 5 5 5 5 5 5
8 10 5
4 4 4 4 4 4 4 4 4 4
8 10 5
0 0 0 0 0 0 0 0 0 0
8 9 6
0 0 0 0 0 0 0 0 0 0
8 10 5
1 4 2 3 7 8 2 5 6 0
8 10 5
0 1 2 3 4 5 6 7 8 8

"""

