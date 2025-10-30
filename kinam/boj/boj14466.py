'''boj14466 - 소가 길을 건너간 이유 6
소가 길을 건너간 이유는 그냥 길이 많아서이다. 
존의 농장에는 길이 너무 많아서, 길을 건너지 않고서는 별로 돌아다닐 수가 없다.

존의 농장에 대대적인 개편이 있었다. 
이제 작은 정사각형 목초지가 N×N (2 ≤ N ≤ 100) 격자로 이루어져 있다. 
인접한 목초지 사이는 일반적으로 자유롭게 건너갈 수 있지만, 그 중 일부는 길을 건너야 한다. 
농장의 바깥에는 높은 울타리가 있어서 소가 농장 밖으로 나갈 일은 없다.

K마리의 (1 ≤ K ≤ 100,K ≤ N2) 소가 존의 농장에 있고, 각 소는 서로 다른 목초지에 있다. 
어떤 두 소는 길을 건너지 않으면 만나지 못 할 수 있다. 이런 소가 몇 쌍인지 세어보자.
'''
# 기본 NxN 배열은 visited처럼 0값 
# r, c, r', c' 에 해당하는 인덱스를 1로
# 1에서 1로는 못감 길이 있어서
# 이 조건을 통해 BFS수행
# 각 소에 대해서 BFS 수행하고 못찾는 소가 있으면 cnt + 1

import sys
from collections import deque
input = sys.stdin.readline

N, K, R = map(int, input().split()) # K : 소의 마릿수, R : 길

# arr = [[0] * N for _ in range(N)] 필요없는듯

way_position = []
way_set = set()
for _ in range(R):
    r, c, r_dash, c_dash = map(int, input().split())
    # arr[c-1][r-1] = 1
    # arr[c_dash-1][r_dash-1] = 1
    # way_position.append((r-1, c-1, r_dash-1, c_dash-1))
    way_set.add((r-1, c-1, r_dash-1, c_dash-1))
    way_set.add((r_dash-1, c_dash-1, r-1, c-1))

cow_position = []
for _ in range(K):
    i, j = map(int, input().split())
    cow_position.append((i-1, j-1))

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def bfs(start_i, start_j):
    visited = [[0] * N for _ in range(N)]
    q = deque([(start_i, start_j)])
    visited[start_i][start_j] = 1
    cnt = 0
    cow = set()
    while q:
        ci, cj = q.popleft()

        for idx, (i, j) in enumerate(cow_position):
            if ci == i and cj == j:
                cow.add(idx)

        if len(cow) == K:
            return 0
        
        for d in range(4):
            ni, nj = ci + di[d], cj + dj[d]
            if (ci, cj, ni, nj) not in way_set:
                if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                    visited[ni][nj] = 1
                    q.append((ni, nj))
        
    return (K - len(cow))

ans = 0
for i, j in cow_position:
    ans += bfs(i, j)

print(ans // 2)