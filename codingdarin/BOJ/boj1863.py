# 1863 스카이라인 쉬운거 (D3, G4)
import sys
input = sys.stdin.readline

stack = []
# 스카이라인 받아오기
# 어차피 왼쪽부터 보는데 y만 체크해도 될듯??
N = int(input())
count = 0

for i in range(N):
    x, y = map(int, input().split())

    # 현재 높이보다 높은 건물들을 모두 제거 (건물 종료)
    while stack and stack[-1] > y:
        stack.pop()
        count += 1

    # 현재 높이가 0이 아니고, 스택이 비어있거나 스택 top과 다른 높이라면 추가
    if y > 0 and (not stack or stack[-1] != y):
        stack.append(y)

# 남은 건물들 모두 제거
count += len(stack)
print(count)