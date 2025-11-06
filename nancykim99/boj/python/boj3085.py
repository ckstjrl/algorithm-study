'''
BOJ3085 / D2): 사탕 게임

해결 방법 : 구현.
'''

def check(board):
    max_count = 1
    # 모든 행 검사하기
    for i in range(N):
        count = 1
        for j in range(1, N):
            if board[i][j] == board[i][j-1]:
                count += 1
            else:
                count = 1
            max_count = max(max_count, count)
    
    # 모든 열 검사하기
    for j in range(N):
        count = 1
        for i in range(1, N):
            if board[i][j] == board[i-1][j]:
                count += 1
            else:
                count = 1
            max_count = max(max_count, count)
            
    return max_count

N = int(input())
arr = [list(input().strip()) for _ in range(N)]

ans = 0

for i in range(N):
    for j in range(N):

        if j + 1 < N:
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j] 
            ans = max(ans, check(arr))
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j] 

        if i + 1 < N:
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j] 
            ans = max(ans, check(arr)) 
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j] 

print(ans)