# 잃어버린 괄호
"""
세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.
그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.
괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.
"""
import sys
text = sys.stdin.readline().rstrip()
nums = []
before = "0"
current = "0"
for word in text:
    if word == '-':
        nums.append(int(current)+int(before))
        before = "0"
        current = "0"
    elif word == '+':
        before = str(int(current)+int(before))
        current = "0"
    else:
        current += word

if before != "0":
    nums.append(int(current)+int(before))
else:
    nums.append(int(current))

if len(nums) == 1:
    print(nums[0])
else:
    result = nums[0]
    for i in range(1, len(nums)):
        result -= nums[i]
    print(result)