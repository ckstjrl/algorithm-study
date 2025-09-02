N, M = map(int, input().split())
arr = [input() for _ in range(N)]
a = 'WBWBWBWB'
b = 'BWBWBWBW'
arr_1 = [a,b,a,b,a,b,a,b]  # (0,0)이 w인 올바른 체스판
arr_2 = [b,a,b,a,b,a,b,a]  # (0,0)이 b인 올바른 체스판
min_1 = 64  # 다시 칠해야 하는 수 기준
min_2 = 64
for i in range(N-7):
    for j in range(M-7):
        cnt_1 = 0
        cnt_2 = 0
        for p in range(0, 8):  # 8 * 8 순회
            for q in range(0, 8):
                if arr[i+p][j+q] != arr_1[p][q]:  # 올바른 체스판과 비교해서 다르면 cnt + 1
                    cnt_1 = cnt_1 + 1  
                if arr[i+p][j+q] != arr_2[p][q]:
                    cnt_2 = cnt_2 + 1
        if cnt_1 < min_1:  # 최솟값 갱신
            min_1 = cnt_1
        if cnt_2 < min_2:
            min_2 = cnt_2

print(min(min_1, min_2))  # 더 작은값 출력
