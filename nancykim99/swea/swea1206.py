T = 10

# 내 주위 4개 중에 가장 높은 곳과 나와의 차이
for tc in range(1, T+1):
    N = int(input())  # 정수의 개수
    ai = list(map(int, input().split()))  # N개의 정수
    result = 0

    for i in range(2, N-2): # 양쪽 2개씩만 슬라이싱
        if ai[i-2] > ai[i-1]: # 왼쪽에서 a가 클경우
            left = ai[i-2]
        else: # 왼쪽에서 b가 클경우
            left = ai[i-1]
        if ai[i+2] > ai[i+1]: # 오른쪽에서 a가 클경우
            right = ai[i+2]
        else: # 오른쪽에서 b가 클경우
            right = ai[i+1]
        if left > right and ai[i] > left: # 왼쪽이 오른쪽보다 크고, 기준이 왼쪽보다 클 경우
            result += ai[i] - left
        elif right > left and ai[i] > right: # 오른쪽이 왼쪽보다 크거나 같고, 기준이 오른쪽보다 클 경우
            result += ai[i] - right 

    print(f'#{tc}', result)
