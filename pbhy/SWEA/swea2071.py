# 2071. 평균값 구하기
# 테스트 케이스 개수 T
T = int(input())

for tc in range(1, T+1):
    # 10개의 수 받기
    arr = list(map(int, input().split()))
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
        mean_n = round(sum / 10)


    print(f'#{tc} {mean_n}')