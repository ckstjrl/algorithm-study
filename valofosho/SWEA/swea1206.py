# T = int(input())
# for testcase in range(1,T+1):
for test_case in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))
    answer = 0
    for i in range(2,N-2):
        if arr[i-2] > arr [i-1]:
            left = arr[i-2]
        else:
            left = arr[i-1]
        if arr[i+2] > arr[i+1]:
            right = arr[i+2]
        else:
            right = arr[i+1]
        if left > right:
            if arr[i] > left:
                answer += arr[i] - left
        else:
            if arr[i] > right:
                answer += arr[i] - right
    print(f"#{test_case} {answer}")