N = int(input())
conf = []
for _ in range(N):
    conf.append(list(map(int, input().split())))

conf_sorted = sorted(conf, key = lambda x:[x[1],x[0]])

start=0
cnt = 0
for s, e in conf_sorted:
    if s >= start:
        cnt += 1
        start = e
print(cnt)
