# T = int(input()) # 테스트 케이스

T = 1
K = 5
N = 100
M = 20
arr = [6, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 76, 81, 85, 90, 95]


for tc in range(1, T+1):
    # K, N, M = map(int, input().split())
    # arr = list(map(int, input().split()))

    arr = [0] + arr + [N]

    last_charger = 0 # 마지막 충전소
    charge = 0 # 충전 횟수

    for i in range(1, M+2): # 1부터 종점까지
        if arr[i] - arr[i-1] > K: # 정류장과 정류장 사이의 거리가 K보다 크면 운행 불가
            charge = 0
            break
        if arr[i] - last_charger > K: # 마지막 충전소와 현재 거리가 K보다 크면 충전 필요
            charge += 1
            last_charger = arr[i-1] # 이전 충전소 들리기

    print(f'#{tc} {charge}')