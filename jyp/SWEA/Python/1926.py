# 1926 간단한 369게임
N = int(input())
game = []
for i in range(1, N+1):
    clap = 0
    for string in str(i):
        if string in ['3', '6', '9']:
            clap += 1
    if clap:
        game.append('-'*clap)
    else:
        game.append(i)

print(*game)