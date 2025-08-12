'''
20230. 풍선팡 보너스게임2 (D2)
'''

T = int(input())
 
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
 
    m = 0
    for i in range(N):                                          # 센터 좌표 설정
        for j in range(N):
            s = arr[i][j]                                       # 합 변수에 센터 좌표 값 더함.
 
            for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:   # 상하좌우 델타
                for d in range(1, N):                           # 센터에서 상하좌우로 떨어진 거리 (1 -> N-1)
                    ni, nj = i+di*d, j+dj*d
                    if 0 <= ni < N and 0 <= nj < N:             # ni와 nj가 배열 범위를 벗어나지 않으면 값 더함.
                        s += arr[ni][nj]
 
            if m < s:                                           # 현재 합이 최댓값보다 크면 변경.
                m = s
 
    print(f'#{tc} {m}')