from bisect import bisect_right
from math import factorial
import sys
import heapq
from collections import Counter, defaultdict, deque
INF = int(1e9)
def input(): return sys.stdin.readline().rstrip()
def miis(): return map(int, input().split())
def lmiis(): return list(miis())


def f(x):
    assert x >= 0
    if x <= 9:
        return factorial(x)
    div, mod = divmod(x, 10)
    return factorial(mod) + f(div)  # 예) f(321) = 3! + 2! + 1!

# f(?) = 20 이 되는 최솟값을 구하려면,
# 팩토리얼 가능한 가장 큰 수로 최대한 잡아먹도록 Greedy
# 그다음 역순 정렬해야 최솟값


y = int(input())

# !!! Edge Case : y = 1일 때는 1이 아니라 0
if y == 1:
    print(0)
    sys.exit(0)

# 0! = 1, 1 = 1이지만, 1은 반드시 맨 처음에 들어가므로 0을 대신 쓸 일이 없음.
# FACTORIALS = [0] * (14 + 1)  # 1-indexed, 계산해본 결과 15! > int(1e9)
# 두자리수 이상 팩토리얼은 의미없음. f(x)에 들어가면 쪼개지니까.

FACTORIALS = [0] * (9 + 1)  # 1-indexed

FACTORIALS[0] = 1
for i in range(1, 9 + 1):
    FACTORIALS[i] = FACTORIALS[i-1] * i

ans = ''
y_left = y
while y_left:
    idx = bisect_right(FACTORIALS, y_left) - 1
    ans = str(idx) + ans
    y_left -= FACTORIALS[idx]

print(ans)
