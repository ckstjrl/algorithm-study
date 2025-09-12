import sys
input = sys.stdin.readline
N, M = map(int, input().strip().split())
poke = {}
names = {}
for i in range(1,N+1):
    name = input().strip()
    poke[name] = i
    names[str(i)] = name
# print(namebase)
for _ in range(M):
    cmd = input().strip()
    if poke.get(cmd):
        print(poke.get(cmd))
    else:
        print(names.get(cmd))
