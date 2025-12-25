from collections import deque
moves = {
    'R': (1, 0),
    'L': (-1, 0),
    'B': (0, -1),
    'T': (0, 1),
    'RT': (1, 1),
    'LT': (-1, 1),
    'RB': (1, -1),
    'LB': (-1, -1),
    }

ki, ro, N = map(str, input().split())

move = deque(moves[input()] for _ in range(int(N)))
ki_p = [(ord(ki[0]) - 65), int(ki[1]) - 1]
ro_p = [(ord(ro[0]) - 65), int(ro[1]) - 1]


while move:
    x, y = move.popleft()
    if 0 <= ki_p[0] + x < 8 and 0 <= ki_p[1] + y < 8:
        if ki_p[0] + x == ro_p[0] and ki_p[1] + y == ro_p[1]:
            if 0 <= ro_p[0] + x < 8 and 0 <= ro_p[1] + y < 8:
                ki_p[0] += x
                ki_p[1] += y
                ro_p[0] += x
                ro_p[1] += y
        else:
            ki_p[0] += x
            ki_p[1] += y


print(chr(ki_p[0] + 65), end='')
print(ki_p[1] + 1)
print(chr(ro_p[0] + 65), end='')
print(ro_p[1] + 1)