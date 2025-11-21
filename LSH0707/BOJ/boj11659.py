import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))
ij = []
for _ in range(M):
    a, b = map(int, input().split())
    ij.append((a, b))
arr_sum = [0] * (N+1)  # 누적 합 배열(arr_sum[x] => x번 수까지의 합)
for i in range(len(arr)):
    if i == 0:
        arr_sum[i+1] = arr[i]
    else:
        arr_sum[i+1] = arr_sum[i] + arr[i]
for a,b in ij:  # a~b번까지의 합 => (b까지의 합 - (a-1)까지의 합)
    print(arr_sum[b]-arr_sum[a-1])