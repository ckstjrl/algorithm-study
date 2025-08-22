# N*N 크기의 판
# 가로, 세로, 대각선 : 5개 이상
# T : 테스트케이스
# N : 5 <= N <= 20
# o : 돌이 있는 칸
# . : 돌이 없는 칸

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    flag = False

    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 'o':
                cnt += 1
                if cnt >= 5:
                    flag = True
                    break
            else:
                cnt = 0
        if flag:
            break
    
    if not flag: #flag가 앞에서 아직 False인 경우
        for j in range(N):
            cnt = 0
            for i in range(N):
                if arr[i][j] == 'o':
                    cnt += 1
                    if cnt >= 5:
                        flag = True
                        break
                else:
                    cnt = 0
            if flag:
                break
        
    if not flag:
        for k in range(N):
            cnt = 0
            i, j = 0, k
            while i < N and j < N:
                if arr[i][j] == 'o':
                    cnt += 1
                    if cnt >= 5:
                        flag = True
                        break
                else:
                    cnt = 0
                i += 1
                j += 1
            if flag:
                break
        
        if not flag:
            for k in range(1, N):
                cnt = 0
                i, j = k, 0
                while i < N and j < N:
                    if arr[i][j] == 'o':
                        cnt += 1
                        if cnt >= 5:
                            flag = True
                            break
                    else:
                        cnt = 0
                    i += 1
                    j += 1
                if flag:
                    break
    
    if not flag:
        for k in range(N):
            cnt = 0
            i, j = 0, k
            while i < N and j >= 0:
                if arr[i][j] == 'o':
                    cnt += 1
                    if cnt >= 5:
                        flag = True
                        break
                else:
                    cnt = 0
                i += 1
                j -= 1
            if flag:
                break
        
        if not flag:
            for k in range(1, N):
                cnt = 0
                i, j = k, N-1
                while i < N and j >= 0:
                    if arr[i][j] == 'o':
                        cnt += 1
                        if cnt >= 5:
                            flag = True
                            break
                    else:
                        cnt = 0
                    i += 1
                    j -= 1
                if flag:
                    break
    
    if flag:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')