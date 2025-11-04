import sys
input = sys.stdin.readline
N = int(input())
arr = [[] for _ in range(N)]
cnt = -1
for _ in range(N):
    a = input().strip()
    if a == 'ENTER':  # enter 기준으로 나눠서 리스트에 저장
        cnt = cnt + 1
    else:
        arr[cnt].append(a)
ans = 0
for i in range(len(arr)):
    if arr[i]:
        ans = ans + len(set(arr[i]))  # 중복 제거한 값 더하기
print(ans)