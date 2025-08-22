T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
 
    sell = 0
    profit = 0
    for i in range(N-1, -1, -1):
        if sell < arr[i]:
            sell = arr[i]
        else:
            profit = profit + sell - arr[i]
    print(f'#{test_case} {profit}')