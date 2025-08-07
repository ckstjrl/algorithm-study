T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    sum_a = 0
    for i in arr :
        sum_a += i
        # arr 원소들의 총 합을 구해 길이만큼 나누면 평균값
    mean_a = sum_a / len(arr)
    mean_u = round(mean_a)
    # 소수점 첫째자리에서 반올림 해야하므로 round() 사용
    print(f'#{tc} {mean_u}')