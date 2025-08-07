'''
16268. 풍선팡2 (D2)
'''

T = int(input())
 
for tc in range(1, T+1):
    N, M = map(int, input().split())
 
    arr = [list(map(int, input().split())) for _ in range(N)]
 
    max_flower = 0
    for i in range(N):                                          # 센터 좌표 설정
        for j in range(M):
            s = arr[i][j]                                       # 합 변수에 센터 좌표 값 더함.
            for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:   # 상하좌우 델타
                ni, nj = i+di, j+dj                             
                if 0 <= ni < N and 0 <= nj < M:                 # 상하좌우로 움직인 좌표가 배열을 넘지 않으면 값 더함.
                    s += arr[ni][nj]
 
            if max_flower < s:                                  # 현재 좌표의 꽃가루 수 합이 최대값보다 크면 변경.
                max_flower = s
 
    print(f"#{tc} {max_flower}")