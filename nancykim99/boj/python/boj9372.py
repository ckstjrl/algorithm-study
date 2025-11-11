'''
BOJ9372 / D2): 상근이의 여행

해결 방법 : 
시도 1. dfs로 푸는데, 뭔가 이상해서 다시 보니. 이미 방문한 국가를 가도 되는 상황이라. 다 지우고 다시 풀기...
시도 2. 모든 국가가 연결되어 있고, 가장 적은 간선을 돌면 되고, 다른 국가를 거쳐가도 되기에 그냥 국가의 수 - 1 해봤다.
* 뭐야. 어처구니 없어.
'''

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    for i in range(M):
        a, b = map(int, input().split())
    
    print(N-1)

