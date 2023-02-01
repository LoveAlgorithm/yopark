import sys
import heapq
from collections import Counter, defaultdict, deque
INF = int(1e9)
def input(): return sys.stdin.readline().rstrip()
def miis(): return map(int, input().split())
def lmiis(): return list(miis())


T = int(input())
for _ in range(T):
    n, L, F = miis()
    W = sorted(map(lambda x: x[::-1], input().split()))
    ans = 0
    is_used = False
    # n >= 2 보장
    for i in range(len(W) - 1):
        if is_used:
            is_used = False
            continue
        s1, s2 = W[i], W[i + 1]
        # F <= L 보장
        if s1[:F] == s2[:F]:
            ans += 1
            is_used = True
    print(ans)
