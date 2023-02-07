import sys
import heapq
from collections import Counter, defaultdict, deque
INF = int(1e9)
def input(): return sys.stdin.readline().rstrip()
def miis(): return map(int, input().split())
def lmiis(): return list(miis())


# 0^0=0, 1^1=0 / 0^1=1, 1^0=1
# K = 0이라면, 0^0=0 -> 0^0=0 (O) / 1^0=1 -> 1^0=1 (O)
# K = 1이라면, 0^1=1 -> 1^1=0 (O) / 1^1=0 -> 0^1=1 (O)
# 즉, M1 = N1^K로 만들었을 때 M1^K를 하면 N1이 나온다.

# M9를 통해 K를 알아낼 수 있나?

T = int(input())
for t in range(T):
    l = input().split()
    M = []
    for e in l:
        M.append(int(e, 16))
    n = sum(M[:-1])
    print(n ^ M[-1])
