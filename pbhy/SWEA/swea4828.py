# 4828. min max

# 테스트 케이스 T
T = int(input())

for tc in range(1, T+1):
    # 양수의 개수 N
    N = int(input())
    # 양수 N개의 배열
    arr = list(map(int, input().split()))

    max_v = arr[0] # arr의 첫번째 수를 max로 가정
    min_v = arr[0] # arr의 첫번쨰 수를 min으로 가정

    for i in range(1, N):
        if arr[i] > max_v:
            max_v = arr[i] # arr[i]가 더 크면 max 갱신

        if arr[i] < min_v:
            min_v = arr[i] # arr[i]가 더 작으면 min 갱신

        result = max_v - min_v

    print (f'#{tc} {result}')

