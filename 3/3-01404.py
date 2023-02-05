# from math import factorial
from itertools import permutations, combinations
import sys
import heapq
from collections import Counter, defaultdict, deque
INF = int(1e9)
def input(): return sys.stdin.readline().rstrip()
def miis(): return map(int, input().split())
def lmiis(): return list(miis())


l = lmiis()
prob = [[0] * 8 for _ in range(8)]

for i, (a, b) in enumerate(combinations([i for i in range(8)], 2)):
    prob[a][b] = l[i] / 100
    prob[b][a] = 1.0 - (l[i] / 100)


def tournament(case):
    ret = [1.0] * 8
    # 1차전
    for i in range(0, 8, 2):
        a, b = case[i], case[i+1]
        ret[a] *= prob[a][b]
        ret[b] *= prob[b][a]
    # 2차전
    for i in range(0, 8, 4):
        a, b, c, d = case[i], case[i+1], case[i+2], case[i+3]
        new_ret = ret[:]
        new_ret[a] *= ret[c] * prob[a][c] + ret[d] * prob[a][d]
        new_ret[b] *= ret[c] * prob[b][c] + ret[d] * prob[b][d]
        new_ret[c] *= ret[a] * prob[c][a] + ret[b] * prob[c][b]
        new_ret[d] *= ret[a] * prob[d][a] + ret[b] * prob[d][b]
        ret = new_ret
    # 3차전
    a, b, c, d, e, f, g, h = case[0], case[1], case[2], case[3], case[4], case[5], case[6], case[7]
    new_ret = ret[:]
    new_ret[a] *= ret[e] * prob[a][e] + ret[f] * \
        prob[a][f] + ret[g] * prob[a][g] + ret[h] * prob[a][h]
    new_ret[b] *= ret[e] * prob[b][e] + ret[f] * \
        prob[b][f] + ret[g] * prob[b][g] + ret[h] * prob[b][h]
    new_ret[c] *= ret[e] * prob[c][e] + ret[f] * \
        prob[c][f] + ret[g] * prob[c][g] + ret[h] * prob[c][h]
    new_ret[d] *= ret[e] * prob[d][e] + ret[f] * \
        prob[d][f] + ret[g] * prob[d][g] + ret[h] * prob[d][h]
    new_ret[e] *= ret[a] * prob[e][a] + ret[b] * \
        prob[e][b] + ret[c] * prob[e][c] + ret[d] * prob[e][d]
    new_ret[f] *= ret[a] * prob[f][a] + ret[b] * \
        prob[f][b] + ret[c] * prob[f][c] + ret[d] * prob[f][d]
    new_ret[g] *= ret[a] * prob[g][a] + ret[b] * \
        prob[g][b] + ret[c] * prob[g][c] + ret[d] * prob[g][d]
    new_ret[h] *= ret[a] * prob[h][a] + ret[b] * \
        prob[h][b] + ret[c] * prob[h][c] + ret[d] * prob[h][d]
    ret = new_ret

    return ret


def win_prob_r1(a):
    b = a + 1 if a % 2 == 0 else a - 1
    return prob[a][b]


def win_prob_r2(a):
    n = a // 2
    if n == 0:
        c, d = 2, 3
    elif n == 1:
        c, d = 0, 1
    elif n == 2:
        c, d = 6, 7
    else:
        c, d = 4, 5
    return win_prob_r1(c) * prob[a][c] + win_prob_r1(d) * prob[a][d]


def win_prob_r3(a):
    n = a // 4
    if n == 0:
        e, f, g, h = 4, 5, 6, 7
    else:
        e, f, g, h = 0, 1, 2, 3
    return win_prob_r1(e) * win_prob_r2(e) * prob[a][e] + win_prob_r1(f) * win_prob_r2(f) * prob[a][f] + win_prob_r1(g) * win_prob_r2(g) * prob[a][g] + win_prob_r1(h) * win_prob_r2(h) * prob[a][h]


ans = []
for i in range(8):
    r1 = win_prob_r1(i)
    r2 = win_prob_r2(i)
    r3 = win_prob_r3(i)
    ans.append(r1 * r2 * r3)

print(*ans)
