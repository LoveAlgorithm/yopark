import sys
import heapq
from collections import Counter, defaultdict, deque
INF = int(1e9)
def input(): return sys.stdin.readline().rstrip()
def miis(): return map(int, input().split())
def lmiis(): return list(miis())


counter = [0] * (12+1)

n = int(input())
for _ in range(n):
    _, s = input().split()
    month = int(s.split('/')[1])
    counter[month] += 1

for month in range(1, 13):
    print(month, counter[month])
