N = int(input())
arr = list(map(int, input().split()))
arr_sum = [0] * N
for i in range(N):
    if i == 0:
        arr_sum[0] = arr[0]
    else:
        arr_sum[i] = arr_sum[i-1] + arr[i]
arr_sum = [0] + arr_sum  # i번 수까지의 합을 기록한 누적합 배열
max_sum = -float('inf')
for i in range(1, 1+N):
    for j in range(i, N+1):
        x = arr_sum[j] - arr_sum[j-i]  # 연속된 구간 완전탐색 후 최댓값 갱신
        if x > max_sum:
            max_sum = x
print(max_sum)