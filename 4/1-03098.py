import sys
import heapq
from collections import Counter, defaultdict, deque
INF = int(1e9)
def input(): return sys.stdin.readline().rstrip()
def miis(): return map(int, input().split())
def lmiis(): return list(miis())


N, M = miis()
graph = [[] for _ in range(N+1)]  # 1-indexed

for _ in range(M):
    A, B = miis()
    graph[A].append(B)
    graph[B].append(A)

# 모두 친구가 되도록 보장


def is_all_friend():
    for a in range(1, N+1):
        for b in range(1, N+1):
            if a == b:
                continue
            if b not in graph[a]:
                return False
    return True


day = 0
cnts = []
while is_all_friend():
    day += 1
    cnt = 0
    for a in range(1, N+1):
        for friend in graph[a]:
            for friend_of_friend in graph[friend]:
                if friend_of_friend not in graph[a]:
                    graph[a].append(friend_of_friend)
                    graph[friend_of_friend].append(a)
                    cnt += 1
    cnts.append(cnt)

print(day)
for cnt in cnts:
    print(cnt)
