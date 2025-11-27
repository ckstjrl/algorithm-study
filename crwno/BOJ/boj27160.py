N = int(input())

cards = [0] * 4

for _ in range(N):
    card, nm = map(str, input().split())
    if card == 'STRAWBERRY':
        cards[0] += int(nm)
    elif card == 'BANANA':
        cards[1] += int(nm)
    elif card == 'LIME':
        cards[2] += int(nm)
    elif card == 'PLUM':
        cards[3] += int(nm)

if 5 in cards:
    print('YES')
else:
    print('NO')