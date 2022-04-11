# 세훈이의 선물가게
"""
세훈이는 선물가게를 운영한다. 세훈이의 선물가게는 특이하게도 손님이 어떤 선물을 구매할지 선택할 수가 없다.
대신 세훈이의 취향으로 랜덤하게 준비된 선물 중 몇 개를 구매할 것인지, 파란색과 빨간색 중 어떤 색으로 포장 받을 것인지만 결정해 주문할 수 있다.

상민이와 지수는 세훈이의 가게에서 선물 포장을 맡은 아르바이트생이다.
손님들은 파란색 포장지를 원하면 상민이에게, 빨간색 포장지를 원하면 지수에게 주문을 한다.
두 사람은 각자 주문을 받으면 그때부터 포장을 시작하는데, 현재 남아있는 선물 중 가장 앞에 있는 선물을 가져와 포장하고 주문을 받은 개수만큼 이를 반복하는 형태다.
이때 선물 하나를 포장하는 데 상민이는 A초, 지수는 B초가 걸린다.
두 사람 모두 받거나 밀린 주문이 없는데 미리 선물을 가져오거나 포장하는 일은 없으며,
두 사람이 동시에 선물을 가져올 때는 알바짬이 조금 더 있는 상민이가 먼저 가져오고, 지수가 그 뒤의 선물을 가져온다.

세훈이는 어제 구매한 선물이 망가져 있다는 항의 전화를 받았다.
자신이 준비한 선물에는 문제가 없었기에 손님에게 포장지의 색을 물었지만, 손님은 자신이 받은 선물이 무엇인지만 말하며 화를 낼 뿐이었다.
어쩔 수 없이 세훈이는 어제 가게를 방문한 손님들의 주문 내역을 보고 그 선물을 누가 포장했는지 파악하려 한다.

방문한 손님의 수와 각 손님이 주문한 시각, 선택한 포장지, 포장 받을 선물의 개수가 주어졌을 때 상민이와 지수가 각자 어떤 선물들을 포장했는지 알아내는 프로그램을 작성해보자.
"""
import sys

makingTimeBlue, makingTimeRed, customerCount = map(int, sys.stdin.readline().rstrip().split())
blueStartTime = 0
redStartTime = 0
packagedProducts = []


def package(orderQuantity, startTime, selectedTime, color):
    for j in range(orderQuantity):
        product = (startTime + (j * selectedTime), color)
        packagedProducts.append(product)


for i in range(customerCount):
    orderAt, color, orderQuantity = sys.stdin.readline().rstrip().split()
    orderAt = int(orderAt)
    orderQuantity = int(orderQuantity)

    if color == "B":
        selectedTime = makingTimeBlue
        startTime = max(orderAt, blueStartTime)
        package(orderQuantity, startTime, selectedTime, color)
        blueStartTime = startTime + (makingTimeBlue * orderQuantity)
    else:
        selectedTime = makingTimeRed
        startTime = max(orderAt, redStartTime)
        package(orderQuantity, startTime, selectedTime, color)
        redStartTime = startTime + (makingTimeRed * orderQuantity)

sortStandard = ["B", "R"]
packagedProducts.sort(key=lambda x: (x[0], sortStandard.index(x[1])))
blueMade = []
redMade = []
for i in range(len(packagedProducts)):
    if packagedProducts[i][1] == "B":
        blueMade.append(i+1)
    else:
        redMade.append(i+1)
print(len(blueMade))
print(*blueMade)
print(len(redMade))
print(*redMade)


"""
2 2 2
1 B 5
1 R 5

1 2 3
1 B 10
1 R 3
2 R 3


"""