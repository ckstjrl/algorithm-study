import sys
string = list(sys.stdin.readline().strip())
M = int(sys.stdin.readline())
arr = [list(sys.stdin.readline().split()) for _ in range(M)]

left = string
right = []

for i in range(M):
    if arr[i][0] == 'P':
        left.append(arr[i][1])
    elif arr[i][0] == 'L':
        if left:
            right.append(left.pop())
    elif arr[i][0] == 'D':
        if right:
            left.append(right.pop())
    elif arr[i][0] == 'B':
        if left:
            left.pop()
print(''.join(left + right[::-1]))