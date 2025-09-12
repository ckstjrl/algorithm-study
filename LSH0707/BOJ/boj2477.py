K = int(input())
arr = [list(map(int, input().split())) for _ in range(6)]
w = [0, 0]  
h = [0, 0]  
for i in range(6):
    if arr[i][0] == 1 or arr[i][0] == 2:  # [동 서 방향중 가장 큰 값, 인덱스]
        if arr[i][1] > w[0]:
            w[0] = arr[i][1]
            w[1] = i
    if arr[i][0] == 3 or arr[i][0] == 4:  # [남 북 방향중 가장 큰 값, 인덱스]
        if arr[i][1] > h[0]:
            h[0] = arr[i][1]
            h[1] = i
sw = abs(arr[(h[1]-1) % 6][1] - arr[(h[1]+1) % 6][1])  # 세로길이 기준 좌우값차이
sh = abs(arr[(w[1]-1) % 6][1] - arr[(w[1]+1) % 6][1])  # 가로길이 기준 좌우값차이
area = w[0] * h[0] - sw * sh 
ans = area * K  # 면적 * 면적당갯수
print(ans)
