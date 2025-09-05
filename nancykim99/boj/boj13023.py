# BOJ13023. ABCDE
N, M = map(int, input().split())

# 인접리스트
adj_list = [[] * (N) for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

visited = [0] * (N + 1)
ans = 0

# dfs
def find_friend(s, depth):
    global ans
    if depth == 4: # 친구가 4명까지 연결되어야 함
        ans = 1
        return
    visited[s] = 1
    for i in adj_list[s]:
        if not visited[i]:
            visited[i] = 1
            find_friend(i, depth + 1) # 재귀로 1번 돌때마다 depth + 1하기
            visited[i] = 0 # 다시 visited[i] = 0해서 재귀 돌때, 영향 받지 않도록 하기


for i in range(N):
    find_friend(i, 0)
    visited[i] = 0 # 다음 for문 돌때 영향 받지 않도록 초기화
    if ans == 1:
        result = 1
        break
    else:
        result = 0


print(result)