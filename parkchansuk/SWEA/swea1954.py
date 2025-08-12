# 달팽이 숫자 / D2
T = int(input())
for tc in range(1, T+1):
    N = int(int(input()))
    arr = [[0]*N for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0] # 순서대로 우, 하, 좌, 상 이동
    way = 0 # 0:우, 1:하, 2:좌, 3:상
    store = []
    for s in range(1, N*N+1):
        store.append(s)

    i = 0
    j = 0
    for num in range(N*N):
        arr[i][j] = store[num] # 이동하면서 store에 있는 1부터 숫자를 넣어줌 
        
        ni = i + di[way] # 다음 위치 계산하면서 확인
        nj = j + dj[way]
        if N <= ni or N <= nj or ni < 0 or nj < 0 or arr[ni][nj] != 0 :
            way = (way+1) % 4 # way 값이 0, 1, 2, 3을 반복해야하고 조건이 맞을때마다 방향 변경 필요
                              # way를 1씩 더해주고 4로 나누면 나머지가 0, 1, 2, 3 반복하게 됨
        i += di[way]
        j += dj[way] # 현재 위치 저장

    print(f'#{tc}')
    for r in arr:
        print(' '.join(map(str, r))) # arr 한줄씩 뽑아서 출력