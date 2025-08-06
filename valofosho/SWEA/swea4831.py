T = int(input())
for test_case in range(1, T+1):
    K, N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    ls = [0] * (N+K+1)
    for i in arr:
        ls[i] += 1
    # arr[N+1] -> 도착지
    start = 0
    # 만약에 start+K+1이 N+1과 같다면 즉, start + K 가 넘치면 안된다
    future = K
    cnt = 0
    while future < N:
        # ls[start+1:start+K+1] 이 첫 선택지
        new_step = ls[start+1: start+K+1]
        # 충전소가 존재하지 않는다면:
        if 1 not in new_step:
            cnt = 0
            break
        else:
            # idx(1,2,3) -> 
            for i in range(start+K, start, -1):
                if ls[i] == 1:
                    cnt += 1
                    start = i
                    future = start + K
                    break
                else:
                    continue
     
    print(f"#{test_case} {cnt}")