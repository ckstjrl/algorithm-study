import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

result = [float('inf')] * 3
for k in range(N):
    i = k + 1
    j = N - 1
    while i < j:
        if abs(arr[i] + arr[j] + arr[k]) < abs(sum(result)):
            result = [arr[k], arr[i], arr[j]]
        if arr[i] + arr[j] + arr[k] > 0:
            j -= 1
        elif arr[i] + arr[j] + arr[k] < 0:
            i += 1
        else:
            break

for i in result:
    print(i, end=' ')