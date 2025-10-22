# BOJ 9372. 상근이의 여행 (D2 / S4)

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    pair = [[] for _ in range(N+1)]
    
    for _ in range(M):
        a, b = map(int, input().split())
    
    # 신장 트리는 간선 개수가 N - 1
    print(N - 1)        
