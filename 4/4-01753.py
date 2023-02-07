import sys
import heapq
from collections import Counter, defaultdict, deque
INF = int(1e9)
def input(): return sys.stdin.readline().rstrip()
def miis(): return map(int, input().split())
def lmiis(): return list(miis())


V, E = miis()
start = int(input())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = miis()
    graph[u].append((v, w))


def dijkstra(start):
    dist = [INF] * (V+1)
    dist[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        w, now = heapq.heappop(q)
        if dist[now] < w:  # 현재 노드가 이미 다른 곳에서 처리되었다면 무시
            continue
        for nxt, nxt_w in graph[now]:
            cost = w + nxt_w
            if cost < dist[nxt]:
                dist[nxt] = cost
                heapq.heappush(q, (cost, nxt))
    return dist


dist = dijkstra(start)

for d in dist[1:]:
    print(d if d != INF else 'INF')
