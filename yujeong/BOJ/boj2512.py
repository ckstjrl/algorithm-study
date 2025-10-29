# 2512. 예산

N = int(input())
arr = list(map(int, input().split()))   # 예산 요청들 
arr.sort()
limit = int(input())

if sum(arr) <= limit:
    print(max(arr))
else:
    # 시도 1: for문 돌면서 상한액 구하기
    # max_val = 0
    # for i in range(max(arr)-1, min(arr), -1):
    #     temp = sum([min(x, i) for x in arr])
    #     if temp <= limit:
    #         max_val = max(i, max_val)
    #         break
    # print(max_val)

    # 시도 2: 이분탐색으로 상한액 구하기 
    l = 0           # 초기 start: 0
    r = arr[-1]     # 초기 end: 요청 예산 중 최댓값 
    ans = 0
    while l <= r:
        mid = (l+r)//2 
        temp = sum([min(x, mid) for x in arr])  # mid가 상한액일 때 예산 배정 총액 
        if temp <= limit:   # limit보다 작다면 mid를 지금보다 큰 범위에서 탐색 
            ans = mid
            l = mid + 1
        else:               # limit보다 크다면 mid를 지금보다 작은 범위에서 탐색
            r = mid - 1
    print(ans)
