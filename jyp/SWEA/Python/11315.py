T = int(input())

def omok(arr, N):
    for i in range(N):
        for j in range(N-4):
            if arr[i][j] == 'o':
                if arr[i][j:j+5] == ['o']*5:
                    return 'YES'
                
            if arr[j][i] == 'o':
                for k in range(5):
                    if arr[j+k][i] != 'o' :
                        break
                else:
                    return 'YES'
                
                if i < N-4:
                    for k in range(5):
                        if arr[i+k][j+k] != 'o':
                            break
                    else:
                        return 'YES'
            if i < N-4 and arr[i][j+4] == 'o':
                for k in range(5):
                    if arr[i+k][j+4-k] != 'o':
                        break
                else:
                    return 'YES'

    return 'NO'

for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    
    result = omok(arr, N)
    print(f'#{tc} {result}')