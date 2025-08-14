# 8.11 2005.파스칼의 삼각형/D2
T = int(input())
for tc in range(1, T+1):
    N = int(input())

    arr = [[1]*N for _ in range(0, N)] # 1로 가득찬 이차원 배열 생성

    if N > 2:
        for a in range(2, N):
            for b in range(1, a):
                arr[a][b] = arr[a-1][b-1] + arr[a-1][b]
                # 위 행에 있는 열 두개를 더해서 아래 행의 열에 넣어줌

    print('#'+str(tc))
    for i in range(N):
        row = arr[i][0:i+1]
        print(' '.join(map(str, row)))
