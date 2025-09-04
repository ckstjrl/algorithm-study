"""
L: idx - 1 if idx == 0 > still
D: idx + 1 if idx == len > still
B: delete stack[idx], if idx == 0 > still
P $: $ 를 커서 왼쪽에 추가 -> insert $ idx
a b c d e
1 -> cursor = 5 a b c d e |
L -> cursor = 4 a b c d | e
L -> cursor = 3 a b c | d e
B -> cursor = 2 a b | d e
P -> cursor = 3 a b P | d e
"""



import sys
input = sys.stdin.readline
# 두 개의 좌, 우 스택을 활용한 풀이
# 커서를 기준으로 좌, 우 나누어서 활용
left = list(input().strip())
right = list()
N = int(input())
command = list(input().split() for _ in range(N))
for cmd in command:
    # L 연산은 커서를 왼쪽으로 옮긴다.
    # 즉, Left의 마지막 요소를 Right로 옮긴다
    if cmd[0] == "L":
        if left:
            right.append(left.pop())
    # R 연산은 커서를 왼쪽으로 옮긴다.
    # 즉, Rightt의 마지막 요소를 Left로 옮긴다
    elif cmd[0] == "D":
        if right:
            left.append(right.pop())
    # B 연산은 커서 왼쪽의 문자를 지운다
    elif cmd[0] == "B":
        if left:
            left.pop()
    # 커서 왼쪽에 $를 삽입
    else:
        left.append(cmd[1])
# 스택은 LIFO 구조이므로 Reverse
r = list(reversed(right))
print(''.join(left) + ''.join(r))




# 시간 초과로 사망
# def L(head):
#     if head != 0:
#         head -= 1   
#     return head

# def D(head, end):
#     if head < end:
#         head += 1
#     return head

# def B(head, end):
#     if head != 0:
#         stack.pop(head-1)
#         head -= 1
#         end -= 1
#     return head, end

# def P(head, value, end):
#     stack.insert(head, value)
#     head += 1
#     end += 1
#     return head, end

# import sys
# input = sys.stdin.readline

# stack = list(input().strip())
# N = int(input())
# command = list(input().split() for _ in range(N))
# cnt = len(stack)
# head = cnt
# for cmd in command:
#     if cmd[0] == "L":
#         head = L(head)
#     elif cmd[0] == "D":
#         head = D(head, cnt)
#     elif cmd[0] == "B":
#         head ,cnt = B(head, cnt)
#     else:
#         head, cnt = P(head, cmd[1], cnt)

# print(''.join(stack))




