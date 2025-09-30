import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
X = int(input())

arr.sort()
cnt = 0
left, right = 0, N - 1

while left < right:
    sum = arr[left] + arr[right]
    if sum == X:
        cnt += 1
        left += 1
    elif sum > X:
        right -= 1
    else:
        left += 1

print(cnt)