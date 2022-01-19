# 습격자 초라기
"""
초라기는 한국의 비밀국방기지(원타곤)를 습격하라는 임무를 받은 특급요원이다.
원타곤의 건물은 도넛 형태이며, 초라기는 효율적인 타격 포인트를 정하기 위해 구역을 아래와 같이 두 개의 원 모양으로 나누었다.
(그림의 숫자는 각 구역의 번호이다.)

초라기는 각각 W명으로 구성된 특수소대를 다수 출동시켜 모든 구역에 침투시킬 예정이며,
각 구역 별로 적이 몇 명씩 배치되어 있는지는 초라기가 모두 알고 있다. 특수소대를 아래 조건에 따라 침투 시킬 수 있다.

한 특수소대는 침투한 구역 외에, 인접한 한 구역 더 침투할 수 있다.
(같은 경계를 공유하고 있으면 인접 하다고 한다. 위 그림에서 1구역은 2, 8, 9 구역과 서로 인접한 상태다.)
즉, 한 특수소대는 한 개 혹은 두 개의 구역을 커버할 수 있다.
특수소대끼리는 아군인지 적인지 구분을 못 하기 때문에, 각 구역은 하나의 소대로만 커버해야 한다.
한 특수소대가 커버하는 구역의 적들의 합은 특수소대원 수 W 보다 작거나 같아야 한다.
이때 초라기는 원타곤의 모든 구역을 커버하기 위해 침투 시켜야 할 특수 소대의 최소 개수를 알고 싶어 한다.
"""
"""
2022-01-18 실패
"""
import sys
Times = int(sys.stdin.readline().rstrip())
for _ in range(Times):
    N, troops = map(int, sys.stdin.readline().rstrip().split())
    arr = [list(map(int, sys.stdin.readline().rstrip().split())), list(map(int, sys.stdin.readline().rstrip().split()))]
    memo = []
    single_vertical = [2 for _ in range(N)]
    for i in range(N):
        if arr[0][i] + arr[1][i] <= troops:
            single_vertical[i] = 1
    memo.append(single_vertical)
    if N >= 2:
        double_square = [4 for _ in range(N)]
        for i in range(N):
            if arr[0][i]+arr[0][(i+1)%N] <= troops:
                layer_one = 1
            else:
                layer_one = 2
            if arr[1][i]+arr[1][(i+1)%N] <= troops:
                layer_two = 1
            else:
                layer_two = 2
            horizontal_count = layer_one + layer_two
            double_square[i] = min(horizontal_count, single_vertical[i]+single_vertical[(i+1)%N])
        memo.append(double_square)
    if N >= 3:
        triple_square = [6 for _ in range(N)]
        for i in range(N):
            if arr[0][i] + arr[0][(i+1)%N] <= troops or arr[0][(i+1)%N] + arr[0][(i+2)%N] <= troops:
                layer_one = 2
            else:
                layer_one = 3
            if arr[1][i] + arr[1][(i+1)%N] <= troops or arr[1][(i+1)%N] + arr[1][(i+2)%N] <= troops:
                layer_two = 2
            else:
                layer_two = 3
            horizontal_count = layer_one + layer_two
            triple_square[i] = min(horizontal_count, single_vertical[i]+double_square[(i+1)%N], double_square[i]+single_vertical[(i+2)%N])
        memo.append(triple_square)

    for size in range(3, N):
        temp = [(size+1)*2 for _ in range(N)]
        for i in range(N):
            single_left_case = memo[0][i]+memo[size-1][(i+1)%N]
            single_right_case = memo[size-1][i]+memo[0][(i+size)%N]
            double_left_case = memo[1][i]+memo[size-2][(i+2)%N]
            double_right_case = memo[size-2][i]+memo[1][(i+size-1)%N]
            triple_left_case = memo[2][i]+memo[size-3][(i+3)%N]
            triple_right_case = memo[size-3][i]+memo[2][(i+size-2)%N]
            temp[i] = min(single_left_case, single_right_case, double_left_case, double_right_case, triple_left_case, triple_right_case)
        memo.append(temp)
    # for mem in memo:
    #     print(*mem)
    print(min(memo[N-1]))


    # if N >= 2:
    # for i in range(N)

"""
1
4 30
15 15 10 20
25 20 10 25
ans : 5
1
4 30
15 10 20 15
20 10 25 25
ans : 5

1
1 80
61
20
ans : 2
 
1
4 3
1 1 3 2
2 1 2 1
ans : 5

1
3 3
1 2 2
3 3 2
ans : 5

1
8 100
70 60 55 43 57 60 44 50
58 40 47 90 45 52 80 40
1
2 5
4 2
3 2
"""
"""
2
3 5
3 3 2
2 4 1
7 5
3 3 2 5 2 3 3
2 4 1 5 1 4 2
ans : 3
ans : 5 + 3
"""
"""
1
6 4
1 2 2 2 3 4
2 4 4 3 1 2
ans : 8
1
3 3
1 2 2
3 3 2
ans : 5
"""
"""
[ input ]
14
6 4
1 2 2 2 3 4
2 4 4 3 1 2
3 3
1 2 2
3 3 2
3 3
1 2 1
1 2 3
3 3
1 2 1
3 1 3
3 3
3 3 3
2 1 1
3 3
3 2 3
2 3 1
3 2
2 1 1
1 2 1
3 3
2 1 1
2 3 3
3 5
3 2 2
1 4 2
4 3
1 1 3 2
2 1 2 1
4 3
1 1 3 2
2 1 2 1
3 6
2 1 3
1 2 5
1 1
1
1
1 2
1
1

    
[ output ]
8
5
4
4
5
5
4
5
3
5
5
3
2
1
"""