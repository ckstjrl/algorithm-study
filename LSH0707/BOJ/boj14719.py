H, W = map(int, input().split())
rain = list(map(int, input().split()))
def water(idx):
    h = rain[idx]
    l = max(rain[0:idx])  # 해당좌표 기준 왼쪽 최대
    r = max(rain[idx+1:W])  # 해당좌표 기준 오른쪽 최대
    if min(l, r) - h > 0:  # 해당좌표에 물이 고일 수 있으면 계산해서 리턴
        return min(l, r) - h
    else:
        return 0
ans = 0
for i in range(1, W-1):  # 처음과끝제외하고 고일 수 있는 물 계산해서 더하기
    ans = ans + water(i)
print(ans)