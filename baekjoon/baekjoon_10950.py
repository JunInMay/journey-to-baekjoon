# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
count_cases = int(input())
cases = []
for i in range(count_cases):
    cases.append(list(map(lambda str: int(str), input().split())))

for case in cases:
    print(case[0]+case[1])