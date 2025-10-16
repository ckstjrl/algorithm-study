import sys
input = sys.stdin.readline

name = ['ChongChong']
N = int(input())
for _ in range(N):
    a, b = map(str, input().split())
    if a in name:
        name.append(b)
    elif b in name:
        name.append(a)

print(len(set(name)))