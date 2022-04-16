# Incomplete Book
"""
Meorge Arr Arr Gartin, the pirate, is currently writing a series of amazing novels.
Full of inspiration, his first novel only took him k days to write.
However, as time went on, he started writing slower and slower. In particular, if it took him ℓ days to write the ith book in the series,
then it will take him 2ℓ days to write the (i + 1)th book.

Because of how slow he is writing the series, fans are worried that he will not be around long enough to finish the series before he dies.
What is the maximum number of books that he can finish before he dies?
"""
import sys

k, D = map(int, sys.stdin.readline().rstrip().split())
days_gone = 0
count = 0

while days_gone < D:
    count += 1
    days_gone += k
    if days_gone > D:
        count -= 1
    k *= 2
print(count)