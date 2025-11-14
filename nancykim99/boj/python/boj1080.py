'''
BOJ1080 : 행렬 (S1)

해결 방법 : 왼위쪽에서부터 하나씩 다르면 돌리기
잘 봐야하는 부분 : 
    1. 3*3보다 작으면 안 돌아감
    2. 3*3보다 작아도 같으면 0으로 정답처리
    3. 끝까지 갔는데도, 같지 않으면, 안 됨

메모 : 이게 되네?
'''

n, m = map(int, input().split())

change_arr = [list(map(int, input().strip())) for _ in range(n)]
ans_arr = [list(map(int, input().strip())) for _ in range(n)]

if change_arr == ans_arr:
    print(0)
    exit()

if n < 3 or m < 3:
    print(-1)
    exit()

cnt = 0
for i in range(n-2):
    for j in range(m-2):
        if change_arr[i][j] != ans_arr[i][j]:
            cnt += 1
            for k in range(i, i+3):
                for l in range(j, j+3):
                    if change_arr[k][l] == 0:
                        change_arr[k][l] = 1
                    else:
                        change_arr[k][l] = 0

if change_arr == ans_arr:
    print(cnt)
else:
    print(-1)