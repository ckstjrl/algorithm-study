N, M = map(int, input().split())

scores = [0] * 6

for i in range(2):
    a, b, c = map(int, input().split())
    scores[3 * i] = a
    scores[3 * i + 1] = b
    scores[3 * i + 2] = c

cnt = 0


def f(start, score, day):
    global cnt
    if day == N:
        if score >= M:
            cnt += 1
            return
        else:
            return
    for k in range(6):
        if start % 3 == k % 3:
            f(k, score + scores[k] // 2, day + 1)
        elif start % 3 != k % 3:
            f(k, score + scores[k], day + 1)


for i in range(6):
    f(i, scores[i], 1)
print(cnt)
