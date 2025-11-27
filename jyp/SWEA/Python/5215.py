T = int(input())
for t in range(1, T + 1):
    N, cal_lim = map(int, input().split())
    food = [list(map(int, input().split())) for _ in range(N)]
    
    # dp[i]는 i 칼로리 내에서 얻을 수 있는 최대 점수
    dp = [0] * (cal_lim + 1)
    
    for score, cal in food:
        # 칼로리 제한치부터 현재 재료의 칼로리까지 역순으로 순회
        for i in range(cal_lim, cal - 1, -1):
            # 현재 재료를 포함하는 경우와 포함하지 않는 경우 중 더 큰 값으로 업데이트
            dp[i] = max(dp[i], dp[i - cal] + score)
        print(dp)
    print(f'#{t} {dp[cal_lim]}')
    