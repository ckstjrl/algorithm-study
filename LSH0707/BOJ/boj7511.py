import sys
input = sys.stdin.readline
from collections import deque
def friend(u, group_n):
    q = deque()
    q.append(u)
    visited[u] = 1
    group[u] = group_n
    while q:
        cur = q.popleft()
        for i in arr[cur]:
            if visited[i] == 0:
                group[i] = group_n  # 시작 유저부터 같은 그룹 숫자 할당
                visited[i] = 1
                q.append(i)
    return
T = int(input())
for test_case in range(1, 1+T):
    print(f'Scenario {test_case}:')
    n = int(input())  # 유저의 수
    k = int(input())  # 친구 관계의 수
    arr = [[] for _ in range(n)]  # 친구 관계
    for _ in range(k):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)
    m = int(input())
    find = []
    for _ in range(m):
        u, v = map(int, input().split())
        find.append((u, v))
    visited = [0] * n
    group = [0] * n
    group_s = 1  # 그룹 숫자 초기화
    for i in range(n):
        if visited[i] == 0:
            friend(i, group_s)  # 그룹숫자 배정
            group_s = group_s + 1  # 다음 그룹 
    for x in range(m):
        u, v = find[x][0], find[x][1]
        if group[u] == group[v]:  # 같은 그룹이면 1 아니면 0
            print(1)
        else:
            print(0)
    print()