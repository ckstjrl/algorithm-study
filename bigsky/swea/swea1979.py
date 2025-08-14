# swea1979: 어디에 단어가 들어갈 수 있을까
T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle_arr = [input().split() for _ in range(N)]
    result = 0
    for i in range(N):
        cnt1 = cnt2 = 0
        for j in range(N):
            # 행 검사
            if puzzle_arr[i][j] == '1':
                cnt1 += 1
                if (j + 1) >= N or puzzle_arr[i][j + 1] == '0':
                    if cnt1 == K:
                        result += 1
                    cnt1 = 0
            #열 검사
            if puzzle_arr[j][i] == '1':
                cnt2 += 1
                if (j + 1) >= N or puzzle_arr[j + 1][i] == '0':
                    if cnt2 == K:
                        result += 1
                    cnt2 = 0
    print(f'#{tc} {result}')
