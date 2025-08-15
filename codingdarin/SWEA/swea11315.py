

def omok(n, arr):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'o':
                cnt = 1
                #가로 체크
                for k in range(1,5):
                    if 0 <= j+k < n and arr[i][j+k] == 'o':
                        cnt +=1
                if cnt == 5:
                    return 'YES'

                #세로 체크
                cnt = 1
                for k in range(1,5):
                    if 0 <= i + k < n and arr[i+k][j] == 'o':
                        cnt += 1
                if cnt == 5:
                    return 'YES'

                #주대각선 체크
                cnt = 1
                for k in range(1,5):
                    if 0 <= i+k < n and 0 <= j+k < n and arr[i+k][j+k] == 'o':
                        cnt += 1
                if cnt == 5:
                    return 'YES'

                #부대각선 체크
                cnt = 1
                for k in range(1,5):
                    if 0 <= i+k < n and 0 <= j-k < n and arr[i+k][j-k] == 'o':
                        cnt += 1
                if cnt == 5:
                    return 'YES'
    return 'NO'   # 모든 검사로 오목이 미발견되었을 경우 NO 반환


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    test_arr = [list(input()) for _ in range(N)]

    ans = omok(N, test_arr)

    print(f"#{tc} {ans}")