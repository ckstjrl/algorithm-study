C = int(input())
for test_case in range(1, 1+C):
    arr = list(map(int, input().split()))
    avg = sum(arr[1:])/arr[0]  # 평균점수
    cnt = 0
    for i in range(1, arr[0]+1): # 평균넘는 사람 수 
        if arr[i] > avg:
            cnt =  cnt + 1   
    print('{0:.3f}'.format(cnt*100/arr[0]), end='')  # 소숫점 3자리까지 출력
    print('%')