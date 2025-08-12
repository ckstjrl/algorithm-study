'''
2072. 홀수만 더하기
'''

T = int(input())

for test_case in range(1, T+1):
    arr = list(map(int, input().split()))   # 값 입력
    sum = 0 

    for i in range(10):                     # 입력받은 정수 10개의 값에서
        if arr[i] % 2 != 0:                 # 값이 홀수라면
            sum += arr[i]                   # sum에 더하기

    print(f'#{test_case} {sum}')