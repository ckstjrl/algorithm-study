import sys
input = sys.stdin.readline

def check_consis(arr):
    for i in range(N):
        for j in range(i + 1, N):
            if arr[i] == arr[j][0:len(arr[i])]:
                return 'NO'
    return 'YES'

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(input().strip())
    arr = sorted(arr, key=len)

    print(check_consis(arr))