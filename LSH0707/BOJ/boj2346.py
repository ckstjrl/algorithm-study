N = int(input())
arr = list(map(int, input().split()))
arr_1 = list(range(1, 1+N))
ans = []
p = 0
while len(arr_1) > 1:
    ans.append(arr_1.pop(p)) # 갱신한 p값으로 pop
    a = arr.pop(p)
    if a > 0:
        p = (p + a - 1) % len(arr_1)  # 양수인 경우 리스트 길이가 -1된 상태에서 현재위치기준 1만큼 덜이동해야 다음 풍선인덱스
    else:
        p = (p + a) % len(arr_1)   # 음수인 경우 왼쪽으로 이동하므로 상관x
ans.append(arr_1[0])
print(*ans)