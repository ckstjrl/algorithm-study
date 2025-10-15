import heapq

N, M, X = map(int, input().split())

route = [[] for _ in range(N + 1)]
for _ in range(M):
    start, end, time = map(int, input().split())
    route[start].append((end, time))


def f(x):
    times = [float('inf')] * (N + 1)
    times[x] = 0
    pq = [(0, x)]

    while pq:
        time_now, point_now = heapq.heappop(pq)

        if time_now > times[point_now]:
            continue

        for point_after, t in route[point_now]:
            time = time_now + t

            if time < times[point_after]:
                times[point_after] = time
                heapq.heappush(pq, (time, point_after))
    return times
res = 0
for i in range(1, N + 1):
    if res < f(i)[X] + f(X)[i]:
        res = f(i)[X] + f(X)[i]
print(res)