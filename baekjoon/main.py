a, b = map(int, input().split())
c = list(map(int, input().split()))

for i in range(a) :
   if c[i] < b :
       print(c[i])



a, b = map(int, input().split())
c = list(map(int, input().split()))

for i in range(a):
    if c[i] >= b:
        del c[i]

print(c)