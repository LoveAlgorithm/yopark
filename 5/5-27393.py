from itertools import permutations
import sys
import heapq
from collections import Counter, defaultdict, deque
INF = int(1e9)
def input(): return sys.stdin.readline().rstrip()
def miis(): return map(int, input().split())
def lmiis(): return list(miis())


l = lmiis()
candidates = []


def dfs(i, n):
    if i == 3:
        if n >= 0:
            candidates.append(n)
        return
    dfs(i+1, n + l[i])
    dfs(i+1, n - l[i])
    dfs(i+1, n * l[i])
    if n % l[i] == 0:
        dfs(i+1, n // l[i])


dfs(1, l[0])
print(min(candidates))
