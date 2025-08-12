T = int(input())

for t in range(1, T+1):
    n = int(input())
    arr = []
    farm = 0

    for _ in range(n):
        arr.append(list(map(int, input())))

    for i in range(n):
        mid = n//2                           # 배열의 중간값
        if i <= mid:                                     # 배열의 중간까지 가운데 열에서 양쪽으로 1씩 범위를 넓혀서 합을 구함
            farm += sum(arr[i][mid-i:mid+i+1])

        else:
            farm += sum(arr[i][mid-(n-i-1):mid+(n-i)])   # 배열의 중간 이후부터 n-i 만큼의 범위를 
    print(f'#{t} {farm}')
