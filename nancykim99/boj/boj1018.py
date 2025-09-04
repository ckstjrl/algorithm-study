# BOJ1018. 체스판 다시 칠하기

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

cnt_arr = []

for i in range(N-8+1):
    for j in range(M-8+1):
        cnt_black = 0
        cnt_white = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k + l) % 2 == 0: 
                    if arr[k][l] != 'B':
                        cnt_black += 1
                    if arr[k][l] != 'W':
                        cnt_white += 1
                else:
                    if arr[k][l] != 'B':
                        cnt_white += 1
                    if arr[k][l] != 'W':
                        cnt_black += 1
        cnt_arr.append(cnt_black)
        cnt_arr.append(cnt_white)


ans = min(cnt_arr)

print(ans)






