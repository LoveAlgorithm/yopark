import sys
import heapq
from collections import Counter, defaultdict, deque
INF = int(1e9)
def input(): return sys.stdin.readline().rstrip()
def miis(): return map(int, input().split())
def lmiis(): return list(miis())


N = int(input())
now = 1
is_increasing = True
for _ in range(N):
    op, time = input().split()
    time = int(time)
    if op == 'HOURGLASS':
        if now == time:
            print(now, 'NO')  # 과부하의 원칙으로 시간 역행도 못하고 중앙 내리치지도 못함
        else:
            print(now, 'NO')
            is_increasing = not is_increasing
    else:
        if now == time:
            print(now, 'YES')
        else:
            print(now, 'NO')

    now = now + 1 if is_increasing else now - 1
    if now == 1 - 1:
        now = 12
    elif now == 12 + 1:
        now = 1
