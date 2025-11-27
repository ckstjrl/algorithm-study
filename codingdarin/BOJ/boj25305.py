# BOJ 25305. 커트라인 (D1/B2)

n, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort(reverse=True)

print(arr[k-1])
