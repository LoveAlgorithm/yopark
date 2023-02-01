import sys
import heapq
from collections import Counter, defaultdict, deque
INF = int(1e9)
def input(): return sys.stdin.readline().rstrip()
def miis(): return map(int, input().split())
def lmiis(): return list(miis())


T = int(input())
for _ in range(T):
    A, B, X = miis()
    R = []
    now = A
    while True:
        if now < B:
            now += A
            continue
        if R and now % B == R[0]:
            break
        R.append(now % B)
        now += A
    R.sort()
    # 0을 도달하는 건 안 치므로 -1
    print(len(R) * (X // B) + len([n for n in R if n <= X % B]) - 1)
