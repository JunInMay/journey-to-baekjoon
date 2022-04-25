import sys

number1, number2 = sys.stdin.readline().rstrip().split()
while not(number1 == "0" and number2 == "0"):
    carryCount = 0
    carry = 0
    maxLen = max(len(number1), len(number2))
    number1 = number1[::-1] + "0" * abs(maxLen - len(number1))
    number2 = number2[::-1] + "0" * abs(maxLen - len(number2))

    for i in range(maxLen):
        if int(number1[i]) + int(number2[i]) + carry >= 10:
            carry = 1
            carryCount += 1
        else:
            carry = 0
    print(carryCount)

    number1, number2 = sys.stdin.readline().rstrip().split()