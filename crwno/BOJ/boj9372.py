T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    route = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        route[a].append(b)
        route[b].append(a)
    print(N - 1)