# 1863. 스카이라인 쉬운거
import sys
input = sys.stdin.readline

N = int(input())

cnt = 0         # 건물 개수 세기
heights = []    # 남아 있는 건물들 높이 저장

for _ in range(N):
    x, y = map(int, input().split())

    # 현재 마지막으로 본 건물 높이보다 새 y가 작으면
    # 그동안 본 y보다 큰 건물들이 모두 종료되었다는 뜻
    # 그만큼 heights에서 pop하고 건물 개수 증가
    while heights and heights[-1] > y:
        heights.pop()
        cnt += 1
    
    # y가 마지막으로 본 건물 높이와 같으면 새 건물 아님
    # 개수 카운트나 스택 요소 조절 없이 continue 
    if heights and heights[-1] == y:
        continue

    # y가 0이면 건물이 아니므로 0이 아닐 때만 새 건물 높이로 append
    if y > 0:
        heights.append(y)

# 그리고 스택에 남아 있는 건물들 개수도 더하기 
cnt += len(heights)

print(cnt)