# BOJ3052. 나머지

arr = []
ans = 0
for i in range(10):
    n = int(input())
    arr.append(n % 42)
    if arr.count(arr[i]) == 1:
        ans += 1


print(ans)










