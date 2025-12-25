board = input()
ans = []
stack = []

for i in board:
    if i != '.':
        stack.append(i)
    else:
        if len(stack) % 2 == 0:
            ans += (len(stack) - (len(stack) % 4)) * ['A']
            ans += (len(stack) % 4) * ['B']
            ans += ['.']
        else:
            break
        stack = []
if len(stack) % 2 == 0:
    ans += (len(stack) - (len(stack) % 4)) * ['A']
    ans += (len(stack) % 4) * ['B']
    print(''.join(ans))
else:
    print(-1)
