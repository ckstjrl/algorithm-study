# 1325. 효율적인 해킹

import sys
input = sys.stdin.readline

N, M = map(int, input().split())    # 컴퓨터 N개, 관계 M개
computers = [[] for _ in range(N+1)]    # 컴퓨터들 간 관계로 인접 리스트
for _ in range(M):
    a, b = map(int, input().split())
    computers[b].append(a)  # b 해킹 시 -> a 가능 

# dfs로 탐색하며 해킹 가능한 컴퓨터 기록하기
def search(s):
    visited = [False] * (N+1)
    stack = [s]
    visited[s] = True

    while stack:
        curr = stack.pop()
        for nxt in computers[curr]:
            if not visited[nxt]:
                stack.append(nxt)
                visited[nxt] = True

    return sum(visited)     # s번 컴퓨터 해킹했을 때 해킹 가능한 컴퓨터 수

max_v = 0
ans = []
# 1번 ~ N번 컴퓨터에서 해킹 시작했을 때 해킹되는 최대 컴퓨터 수 갱신
for i in range(1, N+1):
    cnt = search(i)
    if cnt > max_v:     # 더 큰 값이면 max_v 갱신
        max_v = cnt
        ans = [i]
    elif cnt == max_v:  # 같은 값이면 추가
        ans.append(i)

print(*ans)
