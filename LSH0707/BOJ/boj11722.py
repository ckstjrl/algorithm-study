N = int(input())
arr = list(map(int, input().split()))

max_len = [1] * N  # 초기값 -> 자기 자신 : 1
for i in range(N):
    for j in range(i):
        if arr[j] > arr[i]:  # 앞에 있는 수가 더 크면 i인덱스에서의 최대수열길이 갱신
            max_len[i] = max(max_len[i], max_len[j]+1)

print(max(max_len))