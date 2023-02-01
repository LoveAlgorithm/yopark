from functools import cmp_to_key
import sys
import heapq
from collections import Counter, defaultdict, deque
INF = int(1e9)
def input(): return sys.stdin.readline().rstrip()
def miis(): return map(int, input().split())
def lmiis(): return list(miis())


# https://stackoverflow.com/questions/12749398/using-a-comparator-function-to-sort
X_FIRST, Y_FIRST = -1, 1


def f(X: str, Y: str) -> int:
    if len(X) < len(Y):
        if X == Y[:len(X)]:
            return X_FIRST
    elif len(Y) < len(X):
        if Y == X[:len(Y)]:
            return Y_FIRST
    for c1, c2 in zip(X, Y):
        if c1 == c2:
            continue
        if c1 == '-' and c2 != '-':
            return Y_FIRST
        if c2 == '-' and c1 != '-':
            return X_FIRST
        if c1.lower() != c2.lower():
            return X_FIRST if c1.lower() < c2.lower() else Y_FIRST
        # c1 != c2 인데 c1.lower() == c2.lower()라면 대소문자 무조건 차이나는 것 보장
        return X_FIRST if c1.isupper() else Y_FIRST
    return 0  # 같은 문자열


T = int(input())
for _ in range(T):
    n = int(input())
    l = sorted([input() for _ in range(n)], key=cmp_to_key(f))
    for s in l:
        print(s)
