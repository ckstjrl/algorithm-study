# 18111. 마인크래프트

# 세로 N, 가로 M, 인벤토리 블럭 개수 B
N, M, B = map(int, input().split())

# 집터의 기존 높이들을 기록
cnt_lst = [0] * 257
for _ in range(N):
    for x in map(int, input().split()):
        cnt_lst[x] += 1

# 기존 최소 높이와 기존 최대 높이
# 평준화된 땅의 높이는 무조건 이 값들 사이 값으로 존재
min_h = min(c for c in range(257) if cnt_lst[c])
max_h = max(c for c in range(257) if cnt_lst[c])

# 평준화된 땅의 높이 
target_lvl = 0 

# 평준화까지 걸리는 시간
ans = 500*500*256*2

for i in range(min_h, max_h+1):             # 목표 높이(평준화한 높이) i마다
    inblock, outblock = 0, 0                # 제거할 블록 개수, 쌓을 블록 개수 
    for h in range(257):                    # 기존 땅과 비교
        if not cnt_lst[h]:
            continue    
        if h > i:                           # 기존 높이 h보다 i가 작으면 블록 쌓아야 함
            inblock += (h-i) * cnt_lst[h]   # 쌓아야 하는 개수 * 쌓아야 하는 영역 수 
        else:                               # 아니면 블록 제거해야 함
            outblock += (i-h) * cnt_lst[h]  # 제거해야 하는 개수 * 제거해야 하는 영역 수

    if inblock + B < outblock:              # 새로 얻는 블록 + 인벤토리 블럭으로 쌓을 수 없음
        continue                            
    temp = inblock*2 + outblock             # 제거하는 시간 2초, 쌓는 시간 1초 
    
    if temp <= ans:                         # 기존 최소 시간보다 작으면 갱신
        ans = temp
        target_lvl = i

print(ans, target_lvl)