import sys
import heapq
from collections import Counter, defaultdict, deque
INF = int(1e9)
def input(): return sys.stdin.readline().rstrip()
def miis(): return map(int, input().split())
def lmiis(): return list(miis())


s = input()
words = []
N = int(input())
for _ in range(N):
    words.append(input())

dp = [INF] * (len(s) + 1)
dp[0] = 0


def get_diff(s1, s2):
    assert len(s1) == len(s2)
    ret = 0
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            ret += 1
    return ret


for i in range(1, len(dp) + 1):
    for word in words:
        if i < len(word) or dp[i - len(word)] == -1:
            continue
        candidate = s[i-len(word):i]
        if sorted(list(candidate)) != sorted(list(word)):
            continue
        cost = get_diff(candidate, word)
        dp[i] = min(dp[i], dp[i-len(word)] + cost)

print(dp[len(s)] if dp[len(s)] != INF else -1)
