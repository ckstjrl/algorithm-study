import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    for _ in range(M):
        input().split()
    print(N-1)  # 항상 연결 그래프, 최소신장 트리 -> 간선 = N-1