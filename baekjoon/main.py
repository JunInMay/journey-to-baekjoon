import sys

def bubble(li):
    l = len(li)
    swap = 0
    for i in range(l-1):
        for j in range(l-1-i):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                swap += 1
        print(li)

    result = li[:]
    return result, swap


print(bubble(list(map(int, sys.stdin.readline().rstrip().split()))))