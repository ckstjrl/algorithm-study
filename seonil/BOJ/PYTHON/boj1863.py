"""
1863. 스카이라인 쉬운거

[문제]
도시에서 태양이 질 때에 보이는 건물들의 윤곽을 스카이라인이라고 한다. 스카이라인만을 보고서 도시에 세워진 건물이 몇 채인지 알아 낼 수 있을까? 건물은 모두 직사각형 모양으로 밋밋하게 생겼다고 가정한다.

정확히 건물이 몇 개 있는지 알아내는 것은 대부분의 경우에 불가능하고, 건물이 최소한 몇 채 인지 알아내는 것은 가능해 보인다. 이를 알아내는 프로그램을 작성해 보자.

[입력]
첫째 줄에 n이 주어진다. (1 ≤ n ≤ 50,000) 다음 n개의 줄에는 왼쪽부터 스카이라인을 보아 갈 때 스카이라인의 고도가 바뀌는 지점의 좌표 x와 y가 주어진다. (1 ≤ x ≤ 1,000,000. 0 ≤ y ≤ 500,000) 첫 번째 지점의 x좌표는 항상 1이다.

[출력]
첫 줄에 최소 건물 개수를 출력한다.
"""

import sys

input = sys.stdin.readline

n = int(input())
stack = []
cnt = 0

for _ in range(n):
    x, y = map(int, input().split())

    # 현재 높이가 낮아지는 경우, 스택에서 높은 것들을 pop하면서 건물 끝남을 세기
    while stack and stack[-1] > y:
        stack.pop()
        cnt += 1

    # 현재 높이가 이전과 다르고, 0이 아닌 경우만 push
    if not stack or stack[-1] < y:
        if y != 0:
            stack.append(y)

# 스택에 남은 높이 처리 (0은 건물이 아니므로 무시됨)
cnt += len(stack)

print(cnt)

# 시행착오 - 틀렸던 코드
# 이 코드는 높이가 0인 건물 라인이 들어오는 케이스 일부에서 계산에 오류가 발생한다.
# 생각해보니 x좌표를 굳이 스택에 넣을 필요가 없을 것 같아서 y만 넣는 구조로 바꿨고, 높이가 0인 경우는 스택에 넣지 않는 것으로 수정한 다음 마지막에 스택에 남은 높이를 계산하는 로직을 조금 정리했더니 풀렸다.

# import sys
# input = sys.stdin.readline

# n = int(input())
# stack = []
# cnt = 0
# for _ in range(n):
#     x, y = map(int, input().split())
#     if not stack or y > stack[-1][1]:
#         stack.append((x, y))
#     else:
#         while stack and stack[-1][1] > y:
#             t = stack.pop()
#             cnt += 1

# if not stack:
#     if t[1] >= 1:
#         cnt += 1

# print(cnt)