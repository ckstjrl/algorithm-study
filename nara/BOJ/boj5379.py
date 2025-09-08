import sys
T = int(sys.stdin.readline())
for tc in range(1, 1 + T):
    string = list(sys.stdin.readline().strip())
    left = []
    right = []
    for i in string:
        if i == '<':
            if left:
                right.append(left.pop())
        elif i == '>':
            if right:
                left.append(right.pop())
        elif i == '-':
            if left:
                left.pop()
        else:
            left.append(i)
    print(''.join(left + right[::-1]))