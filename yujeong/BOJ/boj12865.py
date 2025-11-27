# 12865. 평범한 배낭

N, K = map(int, input().split())    # 물건 N개, 총 무게제한 K

weights = [0]   # 각 물건들의 무게 저장
values = [0]    # 각 물건들의 가치 저장 

for _ in range(N):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)

'''
2차원 배열 dp

dp에 저장되는 값: 그 (인덱스) 에서의 최대 가치 
dp의 인덱스: (1) 물건을 몇번까지 보는지 (2) 무게 제한이 얼마인 상황인지

    0   1   2   3   4   <- 인덱스 (몇번 물건까지 봄?)
0   0   0   0   0   0
1   0   0   0   0   0
2   0   0   0   0   0
3   0   0   0   6   0
4   0   0   8   8   0
5   0   0   8   8   12
6   0   13  13  13  13
7   0   13  13  14  14

^ 무게제한

case 1. 지금 이 물건을 넣을 수 없음 -> 안넣은값 (인덱스 -1 덜본것) 저장 
case 2. 지금 이 물건을 넣을 수 있음 -> 
        안넣은값 (인덱스 -1 덜본것) 
        vs. 넣은값 (무게제한이 이 물건 무게만큼 적고 인덱스 -1 덜본것 + 지금가치) 
        중 큰 값 저장
'''

dp = [[0] * (N+1) for _ in range(K+1)]
for w_limit in range(1, K+1):   # 지금 상황에서 무게 제한 (~K까지 늘려가며 봄)
    for idx in range(1, N+1):   # 지금 상황에서 보는 물건 (~N번까지 늘려가며 봄)
        # case 1. 지금 물건을 넣을 수 있음 
        if weights[idx] <= w_limit:
            # 이 물건을 안 넣었을 때 vs. 넣었을 때 중 큰 값 저장 
            dp[w_limit][idx] = max(dp[w_limit][idx-1], dp[w_limit-weights[idx]][idx-1] + values[idx])
        # case 2. 지금 물건을 넣을 수 없음
        else:
            # 이 물건 안 넣었을 때 값 저장 
            dp[w_limit][idx] = dp[w_limit][idx-1]

# 모든 물건을 다 고려하고, 무게 제한이 K인 상황 (= 원래 문제) (= dp[K][N] 에 저장된 값)
print(dp[K][N])