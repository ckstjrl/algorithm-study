N = int(input())
arr = list(map(int, input().split()))
M = int(input())
arr.sort()
idx = -1
total = 0
for i in range(N):  # 어느 지역까지 요청한 금액을 그대로 배정해 줄 수 있는지 인덱스 찾기
    total = total + arr[i]
    if total + arr[i] * (N-i-1) <= M:
        idx = i
if idx == 0:  # 아무지역도 요청한 금액을 못받는경우
    print(M // N)
elif idx == N - 1:  # 모든 지역이 요청한 금액을 받을 수 있는 경우
    print(arr[N-1])
else:  # 배정해줄수 있는 지역까지 해주고 남은 금액 나눠서 배정
    r = M - sum(arr[:idx+1])
    ans = r // (N-1-idx)
    print(ans)