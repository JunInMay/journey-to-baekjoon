# 스타트와 링크
"""
오늘은 스타트링크에 다니는 사람들이 모여서 축구를 해보려고 한다. 축구는 평일 오후에 하고 의무 참석도 아니다.
축구를 하기 위해 모인 사람은 총 N명이고 신기하게도 N은 짝수이다. 이제 N/2명으로 이루어진 스타트 팀과 링크 팀으로 사람들을 나눠야 한다.

BOJ를 운영하는 회사 답게 사람에게 번호를 1부터 N까지로 배정했고, 아래와 같은 능력치를 조사했다.
능력치 Sij는 i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치이다.
팀의 능력치는 팀에 속한 모든 쌍의 능력치 Sij의 합이다. Sij는 Sji와 다를 수도 있으며, i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치는 Sij와 Sji이다.

N=4이고, S가 아래와 같은 경우를 살펴보자.

i\j	1	2	3	4
1	 	1	2	3
2	4	 	5	6
3	7	1	 	2
4	3	4	5
예를 들어, 1, 2번이 스타트 팀, 3, 4번이 링크 팀에 속한 경우에 두 팀의 능력치는 아래와 같다.

스타트 팀: S12 + S21 = 1 + 4 = 5
링크 팀: S34 + S43 = 2 + 5 = 7
1, 3번이 스타트 팀, 2, 4번이 링크 팀에 속하면, 두 팀의 능력치는 아래와 같다.

스타트 팀: S13 + S31 = 2 + 7 = 9
링크 팀: S24 + S42 = 6 + 4 = 10
축구를 재미있게 하기 위해서 스타트 팀의 능력치와 링크 팀의 능력치의 차이를 최소로 하려고 한다. 위의 예제와 같은 경우에는 1, 4번이 스타트 팀, 2, 3번 팀이 링크 팀에 속하면 스타트 팀의 능력치는 6, 링크 팀의 능력치는 6이 되어서 차이가 0이 되고 이 값이 최소이다.
"""
"""
PyPy3으로 틀렸는데(시간초과 X), Python 3으로 통과한 코드 = ???왜???
"""
import sys

players_number = int(sys.stdin.readline().rstrip())
point_table = []
result = float('inf')
for _ in range(players_number):
    point_table.append(list(map(int, sys.stdin.readline().rstrip().split())))


def getTeamPointSum(team_set):
    point_sum = 0
    for subject_candidate in team_set:
        for object_candidate in team_set:
            point_sum += point_table[subject_candidate - 1][object_candidate - 1]
    return point_sum


def distributeTeam(candidate_set=set([x for x in range(1, players_number+1)]), team_start_set=set([]), last_number=0):
    global result
    if len(team_start_set) < (players_number / 2):
        for candidate in candidate_set:
            if candidate > last_number:
                team_start_set.add(candidate)
                candidate_set.remove(candidate)

                distributeTeam(candidate_set, team_start_set, candidate)

                team_start_set.remove(candidate)
                candidate_set.add(candidate)
    else:
        team_link_set = candidate_set
        result = min(abs(getTeamPointSum(team_start_set)-getTeamPointSum(team_link_set)), result)


distributeTeam()
print(result)