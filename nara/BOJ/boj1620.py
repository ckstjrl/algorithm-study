import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
pokemon = dict()
for i in range(1, N + 1):
    name = input().strip()
    pokemon[i] = name
    pokemon[name] = i

problem = [input().strip() for _ in range(M)]

for x in problem:
    if x.isdigit():
        print(pokemon[int(x)])
    else:
        print(pokemon[x])