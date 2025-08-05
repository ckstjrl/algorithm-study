T = int(input()) # 테스트 케이스

for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    N = 10 # 10개의 수

    num_sum = 0
    for i in range(10):
        if arr[i] > 0:
            num_sum += arr[i]

    num_average = round(num_sum / 10)
    print(f'#{tc} {num_average}')
