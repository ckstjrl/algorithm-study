# 1859. 백만 장자 프로젝트 / D2

T = int(input())

for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    high_price = arr[-1] # 마지막 날 매매가
    profit = 0

    # N일 동안의 매매가를 거꾸로 순회하며
    for i in range(N-1, -1, -1):
        if arr[i] > high_price:        # 더 비싼 매매가가 있으면 갱신 
            high_price = arr[i]
        profit += high_price - arr[i]  # 비싼 매매가에서 그날 매매가를 뺀 값
    
    print(f'#{t+1} {profit}')