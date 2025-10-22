# BOJ 16401. 과자 나눠주기 (D2 / S2)

m, n = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 1, max(arr)
answer = 0

while left <= right:
    mid = (left + right) // 2
    
    # mid 길이로 나눠줄 수 있는 조카 수
    count = 0
    for cookie in arr:
        count += cookie // mid
    
    if count >= m:  # 나눠줄 수 있으면 더 긴 길이 시도
        answer = mid
        left = mid + 1
    else:  # 부족하면 길이 줄이기
        right = mid - 1

print(answer)