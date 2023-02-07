import sys
import heapq
from collections import Counter, defaultdict, deque
INF = int(1e9)
def input(): return sys.stdin.readline().rstrip()
def miis(): return map(int, input().split())
def lmiis(): return list(miis())


DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

M, N = miis()
box = []
for _ in range(N):
    box.append(lmiis())


def simulate():
    def get_ripe_tomato_pos_list():
        ret = []
        for i in range(N):
            for j in range(M):
                if box[i][j] == 1:
                    ret.append((i, j, 0))
        return ret

    l = get_ripe_tomato_pos_list()

    q = deque(l)
    ret = 0
    while q:
        y, x, day = q.popleft()
        ret = max(ret, day)
        for dy, dx in DIRS:
            ny, nx = y + dy, x + dx
            if not (0 <= ny < N and 0 <= nx < M):
                continue
            if box[ny][nx] == 1:
                continue
            if box[ny][nx] == -1:
                continue
            box[ny][nx] = 1
            q.append((ny, nx, day + 1))
    return ret


day = simulate()


def is_all_ripe():
    for i in range(N):
        for j in range(M):
            if box[i][j] == 0:
                return False
    return True


print(day if is_all_ripe() else -1)
