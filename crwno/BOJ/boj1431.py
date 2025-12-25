N = int(input())
sentences = [input() for _ in range(N)]


def info(x):
    length = len(x)
    sum_nm = 0
    for i in x:
        if i.isdigit():
            sum_nm += int(i)
    return (length, sum_nm, x)

res = []
for j in range(N):
    res.append(info(sentences[j]))

res.sort(key=lambda x: (x[0], x[1], x[2]))

for k in range(N):
    a, b, c = res[k]
    print(c)
