import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    a = input().strip()
    left = []  # 커서 기준 왼쪽
    right = []  # 커서 기준 오른쪽
    for i in a:
        if i == '<':  # 왼쪽 pop해서 오른쪽에 append (오른쪽은 순서가 거꾸로 append)
            if left:
                right.append(left.pop())
        elif i == '>':  # 오른쪽 pop해서 왼쪽에 append
            if right:
                left.append(right.pop())
        elif i == '-':  # 커서기준 왼쪽 pop
            if left:
                left.pop()
        else:
            left.append(i)  # 커서기준 왼쪽에 문자 append

    print(''.join(left + right[::-1]))  # 오른쪽은 역순