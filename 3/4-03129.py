import sys
import heapq
from collections import Counter, defaultdict, deque
INF = int(1e9)
def input(): return sys.stdin.readline().rstrip()
def miis(): return map(int, input().split())
def lmiis(): return list(miis())


msg = input()
hint = input()


def get_c(from_, to_):
    n, m = ord(from_) - ord('a'), ord(to_) - ord('a')
    if n - m < 0:
        n += 26
    return chr((n - m) + ord('a'))


def get_key_str(from_, to_):
    assert len(from_) == len(to_)
    key_str = ''
    for c1, c2 in zip(from_, to_):
        key_str += get_c(c1, c2)
    return key_str


def is_valid_key(key_str, key):
    for i, c in enumerate(key_str):
        if key_str[i] != key[i % len(key)]:
            return False
    return True


def parse_to_key(key_str):
    assert key_str
    for i in range(1, len(key_str) // 2 + 1):
        # i : key의 예상 길이
        key_candidate = key_str[:i]
        if not is_valid_key(key_str, key_candidate):
            continue
        return key_candidate
    return None  # 이 key_str에서는 반복되는 문자열이 없습니다.


key = ''
for i in range(len(msg) - len(hint) + 1):
    key_str = get_key_str(msg[i:i+len(hint)], hint)
    if parsed_key := parse_to_key(key_str):
        key = parsed_key
        break

assert (key)


def decrypt(msg, key):
    ret = ''
    for i, c in enumerate(msg):
        ret += get_c(msg[i], key[i % len(key)])
    return ret


ret = ''
for i in range(len(key)):
    key = key[-1] + key[:-1]
    org_candidate = decrypt(msg, key)
    if hint in org_candidate:
        ret = org_candidate
        break

assert ret
print(ret)
