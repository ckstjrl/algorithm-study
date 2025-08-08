# 최대수 구하기 / D1
T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))

    # 최댓값 구하기
    max_v = 0
    for i in range(10):
        if max_v < arr[i]:
            max_v = arr[i]
    
    print(f'#{tc} {max_v}')