'''
2071. 평균값 구하기
'''

T = int(input())

for test_case in range(1, T+1):
    arr = list(map(int, input().split()))
    sum = 0

    for i in range(10):
        sum += arr[i]               # 모든 값의 합
    
    if sum % 10 >= 5:               # 평균의 소수점이 0.5 이상일 때 올림
        avg = int(sum / 10) + 1     
    else:
        avg = int(sum / 10)         # 0.5 미만이면 버림
    
    print(f'#{test_case} {avg}')