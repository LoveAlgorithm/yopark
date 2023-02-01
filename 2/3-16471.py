import sys
import heapq
from collections import Counter, defaultdict, deque
INF = int(1e9)
def input(): return sys.stdin.readline().rstrip()
def miis(): return map(int, input().split())
def lmiis(): return list(miis())


N = int(input())
me, you = sorted(lmiis()), sorted(lmiis())

# 큰 차이로 이긴다고 점수를 많이 주는 건 없다.
# 그냥 사장님 제일 작은 거부터 시작해서, 나한테 있는 작은 것 순으로 내면 됨.

cnt = 0
will_use = 0
for e in you:
    if me[will_use] < e:
        cnt += 1
        will_use += 1
        if will_use == N:
            break
print('YES' if cnt >= (N+1) // 2 else 'NO')
