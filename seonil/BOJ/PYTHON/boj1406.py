"""
1406. 에디터

[문제]
한 줄로 된 간단한 에디터를 구현하려고 한다. 이 편집기는 영어 소문자만을 기록할 수 있는 편집기로, 최대 600,000글자까지 입력할 수 있다.
이 편집기에는 '커서'라는 것이 있는데, 커서는 문장의 맨 앞(첫 번째 문자의 왼쪽), 문장의 맨 뒤(마지막 문자의 오른쪽), 또는 문장 중간 임의의 곳(모든 연속된 두 문자 사이)에 위치할 수 있다.
즉 길이가 L인 문자열이 현재 편집기에 입력되어 있으면, 커서가 위치할 수 있는 곳은 L+1가지 경우가 있다.
이 편집기가 지원하는 명령어는 다음과 같다.

* L : 커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
* D    : 커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
* B    : 커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨) 삭제로 인해 커서는 한 칸 왼쪽으로 이동한 것처럼 나타나지만, 실제로 커서의 오른쪽에 있던 문자는 그대로임
P $    : $라는 문자를 커서 왼쪽에 추가함
초기에 편집기에 입력되어 있는 문자열이 주어지고, 그 이후 입력한 명령어가 차례로 주어졌을 때, 모든 명령어를 수행하고 난 후 편집기에 입력되어 있는 문자열을 구하는 프로그램을 작성하시오. 단, 명령어가 수행되기 전에 커서는 문장의 맨 뒤에 위치하고 있다고 한다.

[입력]
첫째 줄에는 초기에 편집기에 입력되어 있는 문자열이 주어진다. 이 문자열은 길이가 N이고, 영어 소문자로만 이루어져 있으며, 길이는 100,000을 넘지 않는다. 둘째 줄에는 입력할 명령어의 개수를 나타내는 정수 M(1 ≤ M ≤ 500,000)이 주어진다. 셋째 줄부터 M개의 줄에 걸쳐 입력할 명령어가 순서대로 주어진다. 명령어는 위의 네 가지 중 하나의 형태로만 주어진다.

[출력]
첫째 줄에 모든 명령어를 수행하고 난 후 편집기에 입력되어 있는 문자열을 출력한다.
"""

import sys

input = sys.stdin.readline

# 초기 문자열 입력
left_stack = list(input().strip())
right_stack = []

# 명령어 개수
M = int(input())

for _ in range(M):
    command = input().split()

    if command[0] == 'L':
        if left_stack:
            right_stack.append(left_stack.pop())
    elif command[0] == 'D':
        if right_stack:
            left_stack.append(right_stack.pop())
    elif command[0] == 'B':
        if left_stack:
            left_stack.pop()
    elif command[0] == 'P':
        left_stack.append(command[1])

# 결과 출력
print("".join(left_stack + right_stack[::-1]))

# 첫 번째 풀이(나의 풀이) : 주어진 3개의 예제 test case는 통과했지만, 시간 초과로 fail
#
# import sys
#
# # 초기 문자열 입력 (리스트로 변환해 문자 단위로 다루기 쉽게 함)
# # sys.stdin.readline()으로 입력받으면 맨 끝에 '\n'이 붙으므로 rstrip('\n')으로 제거
# input_str = list(sys.stdin.readline().rstrip('\n'))
#
# # 커서는 처음에 문자열의 맨 뒤에 위치
# cursor = len(input_str)
#
# # 명령어 개수 입력
# M = int(sys.stdin.readline())
# for _ in range(M):
#     # 명령어 입력 (P $ 같은 경우를 위해 split() 사용)
#     command = sys.stdin.readline().split()
#
#     # L : 커서를 왼쪽으로 이동
#     if command[0] == 'L':
#         if cursor > 0:  # 커서가 맨 앞이 아닐 때만 이동 가능
#             cursor -= 1
#
#     # D : 커서를 오른쪽으로 이동
#     elif command[0] == 'D':
#         if cursor < len(input_str):  # 커서가 맨 뒤가 아닐 때만 이동 가능
#             cursor += 1
#
#     # B : 커서 왼쪽 문자 삭제
#     elif command[0] == 'B':
#         if cursor > 0:  # 커서가 맨 앞이 아닐 때만 삭제 가능
#             del input_str[cursor - 1]  # 커서 왼쪽 문자 삭제
#             cursor -= 1  # 삭제 후 커서를 한 칸 왼쪽으로 이동한 효과
#
#     # P $ : 커서 왼쪽에 문자 삽입
#     elif command[0] == 'P':
#         input_str.insert(cursor, command[1])  # 현재 커서 위치에 문자 삽입
#         cursor += 1  # 삽입 후 커서를 오른쪽으로 이동
#
# # 리스트를 문자열로 합쳐 최종 결과 출력
# print("".join(input_str))
#
# ----------------------------------------------------------------------------------------------------------------
#
# 두 번째 풀이(gpt code를 기반으로 연습한 코드) - 시간 초과로 fail
# sys.stdin.readline()과 input()을 혼용해서 써서 이런 문제가 발생한듯! 정수 하나 입력받을 때라고 input()을 혼용하는 행동은 하지 말자.
# 
# import sys
# 
# # 초기 문자열 입력
# left_stack = list(sys.stdin.readline().strip())
# right_stack = []
# 
# # 명령어 개수
# M = int(input())
# 
# for _ in range(M):
#     command = input().split()
# 
#     if command[0] == 'L':
#         if left_stack:
#             right_stack.append(left_stack.pop())
#     elif command[0] == 'D':
#         if right_stack:
#             left_stack.append(right_stack.pop())
#     elif command[0] == 'B':
#         if left_stack:
#             left_stack.pop()
#     elif command[0] == 'P':
#         left_stack.append(command[1])
# 
# # 결과 출력
# print("".join(left_stack + right_stack[::-1]))