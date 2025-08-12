# 2072. 홀수만 더하기
# 테스트 케이스 갯수
T = int(input())

for tc in range(1, T+1):
    # 숫자 받기
    arr = list(map(int, input().split()))
    sum = 0
    for i in range(10):
        # 홀수만 하기
        if arr[i] % 2 !=0:
            sum = sum + arr[i]

    print(f'#{tc} {sum}')