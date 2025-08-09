def check(i,j,N):
    if 0<=i<N and 0<=j<N:
        return True
    else:
        return False

def cross(i,j,N,M,arr):
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]
    cur = arr[i][j]
    for d in range(4):
        for c in range(1,M):
            ni = i+di[d]*c
            nj = j+dj[d]*c
            if check(ni,nj,N):
                cur += arr[ni][nj]
            else:
                break
    return cur

def xcross(i,j,N,M,arr):
    di = [1, 1, -1, -1]
    dj = [1, -1, 1, -1]
    cur = arr[i][j]
    for d in range(4):
        for c in range(1,M):
            ni = i+di[d]*c
            nj = j+dj[d]*c
            if check(ni,nj,N):
                cur += arr[ni][nj]
            else:
                break
             
    return cur


T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_sum = 0
    for i in range(N):
        for j in range(N):
            # 각 좌표마다 cross, xcross 검사 후 값 리턴
            cur_max = max(cross(i,j,N,M,arr), xcross(i,j,N,M,arr))
            if max_sum < cur_max:
                max_sum = cur_max

    print(f"#{test_case} {max_sum}")