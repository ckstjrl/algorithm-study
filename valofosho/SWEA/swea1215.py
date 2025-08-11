for test_case in range(1, 11):
    N = int(input())
    maps = [list(input()) for _ in range(8)]
    cnt = 0
    # 동일 행 내의 회문 검사
    for i in range(8):
        for j in range(8-N+1):
            sliced = maps[i][j:j+N]
            if sliced == sliced[::-1]:
                cnt += 1
    # 동일 열 내의 회문 검사
    for j in range(8):
        for i in range(8-N+1):
            arr = []
            for k in range(N):
                arr.append(maps[i+k][j])
            if arr == arr[::-1]:
                cnt += 1
    print(f"#{test_case} {cnt}") 