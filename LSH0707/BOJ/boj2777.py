import sys
input = sys.stdin.readline
T = int(input())
for test_case in range(T):
    N = int(input())
    cnt = [0] * 10
    for i in range(9, 1, -1):  # N을 9~2까지 나눌 수 있을때까지 나누고 몫 기록
        while True:
            if N % i == 0:
                cnt[i] = cnt[i] + 1
                N = N / i
            else:
                break
    if N == 1:  # 9~2까지의 수의 거듭제곱으로 나타낼수 있는 숫자인 경우
        x = sum(cnt)
        if x > 0:  # N!=1인 경우
            print(sum(cnt))
        else:
            print(1)  # N=1인 경우
    else:
        print(-1)