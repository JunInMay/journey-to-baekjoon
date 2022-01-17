inputs = []
for element in map(lambda a:int(a), input().split()):
    inputs.append(element)

year = inputs[0]
leap_year = 0

# if year % 400 == 0:
#     leap_year = 1
# elif year % 100 != 0 & year % 4 == 0:
#     leap_year = 1

if year % 400 == 0:
    leap_year = 1
elif year % 100 == 0:
    leap_year = 0
elif year % 4 == 0:
    leap_year = 1

print(leap_year)