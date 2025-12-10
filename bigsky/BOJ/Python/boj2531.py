# BOJ2531: 회전 초밥
import sys

# N: 접시의 수, d: 초밥 가짓수, k: 연속해서 먹는 접시 수, c: 쿠폰 번호
N, d, k, c = map(int, sys.stdin.readline().split())
sushis = [int(sys.stdin.readline()) for _ in range(N)]

sushi_cnt = [0] * (d + 1)
c_unique_cnt = 0

# 1. 초기 윈도우 설정
for i in range(k):
    if sushi_cnt[sushis[i]] == 0:
        c_unique_cnt += 1
    sushi_cnt[sushis[i]] += 1

max_unique = c_unique_cnt
if sushi_cnt[c] == 0:
    max_unique += 1

# 2. 슬라이딩 윈도우 진행
for s_idx in range(N):
    start = sushis[s_idx]
    sushi_cnt[start] -= 1
    if sushi_cnt[start] == 0:
        c_unique_cnt -= 1

    e_idx = (s_idx + k) % N
    end = sushis[e_idx]
    if sushi_cnt[end] == 0:
        c_unique_cnt += 1
    sushi_cnt[end] += 1

    if sushi_cnt[c] == 0:
        max_unique = max(max_unique, c_unique_cnt + 1)
    else:
        max_unique = max(max_unique, c_unique_cnt)

print(max_unique)