N = int(input())
arr = list(map(int, input().split()))

ans = [arr[0]]
for i in range(1, N):
    if arr[i - 1] < arr[i]:
        ans.append(arr[i - 1] + (i + 1) * (arr[i] - arr[i - 1]))
    elif arr[i - 1] > arr[i]:
        ans.append(arr[i - 1] + (i + 1) * (arr[i] - arr[i - 1]))
    else:
        ans.append(arr[i - 1])
for i in ans:
    print(i, end=' ')
