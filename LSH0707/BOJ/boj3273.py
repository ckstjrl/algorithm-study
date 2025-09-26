import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
x = int(input())
cnt = 0
arr.sort()
i = 0  # 최솟값
j = len(arr) - 1  # 최댓값
while i < j:
    if arr[i] + arr[j] == x:  # 구하는 값이면 cnt+1, 한칸씩 안쪽으로
        cnt = cnt + 1
        i = i + 1
        j = j - 1
    elif arr[i] + arr[j] < x:  # 작으면, 작은값 idx 올려서 더 큰 값 계산
        i = i + 1
    else:  # 크면, 큰값 idx 낮추고 더 작은 값 계산
        j = j - 1
print(cnt)