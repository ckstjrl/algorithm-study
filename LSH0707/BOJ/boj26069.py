import sys
input = sys.stdin.readline
N = int(input())
d = set()
for _ in range(N):
    a, b = input().split()
    if a == 'ChongChong' or b == 'ChongChong':
        d.add(a)
        d.add(b)
    if a in d:
        d.add(b)
    if b in d:
        d.add(a)
print(len(d))