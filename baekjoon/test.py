
li = [i for i in range(4, 1001)]

true_li = []
for l in li:
    if l % 2 == 0:
        true_li.append(l)
print(len(true_li))
for tl in true_li:
    print(tl)