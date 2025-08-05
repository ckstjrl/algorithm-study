T = int(input())
for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    tmp = sum # 반올림 유무를 판단할 임시변수
    tmp = tmp % 10 # 일의자리 숫자 뽑아냄
    result = sum //  len(arr)
    if tmp >= 5: # 반올림
        result += 1
    print(f"#{test_case} {result}")