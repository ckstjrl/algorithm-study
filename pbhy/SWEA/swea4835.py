# 4835. 구간합

# 테스트 케이스 T
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    max_v = 0 # 최댓값을 0으로 가정
    min_v = 0 # 최솟값을 0으로 가정

    for i in range(N-M+1): # 구간 : 0 ~ N-M -> 0 ~ N-M+1
        sum = 0
        for j in range(i, i+M): # j구간의 원소 인덱스 i ~ i+M-1 -> i ~ i+M-1+1
            sum += arr[j]
        if sum > max_v:
            max_v = sum

        if min_v == 0:
            min_v = sum

        if sum < min_v:
            min_v = sum

        result = max_v - min_v

    print(f'#{tc} {result}')
