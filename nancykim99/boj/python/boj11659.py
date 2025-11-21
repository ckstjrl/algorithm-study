'''
BOJ11659 : 구간 합 구하기 4 (S3)

해결 방법 : 
1. a-1부터 b-1까지의 합을 구현해서 풀어보았음 -> 시간 초과
`n, m = map(int, input().split())
arr = list(map(int, input().split()))
ans = []
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    total = 0
    for i in range(a, b):
        total += arr[i]
    ans.append(total)

for i in range(m):
    print(ans[i])`

2. 모든 누적합을 구해서 그 누적합에서 b에서 a-1을 빼는 방식으로 진행 -> 누적합 알고리즘
    일반적으로 부분배열의 합을 구하는 경우 시간복잡도 -> O(N)
    누적합 알고리즘 사용하는 경우 시간복잡도 -> O(1)
'''

n, m = map(int, input().split())
arr = list(map(int, input().split()))
sum = [0] # 누적합 리스트
ans = []

for i in range(n):
    sum.append((sum[i]+arr[i]))

# 누적합 구하기
for i in range(m):
    a, b = map(int, input().split())
    ans.append(sum[b] - sum[a-1])

for i in range(m):
    print(ans[i])