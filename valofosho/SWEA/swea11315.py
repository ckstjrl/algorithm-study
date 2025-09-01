# arr 내 범위 확인 
def check(i,j,N):
    if 0<=i<N and 0<=j<N:
        return True
    else:
        return False

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    flag = False
    for i in range(N):
        if flag: break
        for j in range(N):
            di = [1, 1, 1, -1, -1, -1, 0, 0]
            dj = [1, -1, 0, 1, -1, 0, 1, -1]
            start = arr[i][j]
            # 돌이 있는 곳에서만 찾기
            if start == 'o':
                for d in range(8):
                    cnt = 0
                    # 이미 돌에서부터 시작이므로 동일 방향으로 4번만 반복
                    for c in range(1,5):
                        ni, nj = i+di[d]*c, j+dj[d]*c
                        # 범위 내에 돌이면 카운트
                        if check(ni,nj,N) and arr[ni][nj] == 'o':
                            cnt += 1
                            if cnt == 4:
                                flag = True
                                break
                        else:
                            break
                        
    
    print(f"#{test_case} {'YES' if flag else 'NO'}")