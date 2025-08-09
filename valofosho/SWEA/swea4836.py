T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    ans = 0
    blues = []
    arr = [[0] * 10 for _ in range(10)]
    for _ in range(N):
        r1, c1, r2, c2, c = map(int, input().split())
        if c == 1:
            for i in range(r1, r2+1):
                for j in range(c1, c2+1):
                    arr[i][j] = 1
        else:
            blues.append([r1, c1, r2, c2])
        for blue in blues:
            r1, c1, r2, c2 = blue
            for i in range(r1, r2+1):
                for j in range(c1, c2+1):
                    if arr[i][j] == 1:
                        ans += 1
                        arr[i][j] = 0
    print(f"#{test_case} {ans}")