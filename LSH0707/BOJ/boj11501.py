T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    arr = arr[::-1]  # 거꾸로 순회
    ans = 0  # 이익
    max_value = 0  # 주식 판매 가격 기록
    for i in range(len(arr)):
        if arr[i] > max_value:  # 주식 판매 최대가격 기록
            max_value = arr[i]
        if arr[i] < max_value:  # 판매가가 더 높은경우 이익 갱신
            ans = ans + max_value - arr[i]
    print(ans)