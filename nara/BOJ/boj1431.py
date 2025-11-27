import sys
input = sys.stdin.readline

N = int(input())
guitar = [list(map(str, input().strip())) for _ in range(N)]

result = [[] for _ in range(N)]
for i in range(N-1):
    for j in range(i+1, N):
        # 1. 길이순으로 정렬
        if len(guitar[i]) > len(guitar[j]):
            guitar[i], guitar[j] = guitar[j], guitar[i]

        # 2. 길이가 같은 경우 자리수 합 순으로 정렬
        elif len(guitar[i]) == len(guitar[j]):
            sum1, sum2 = 0, 0
            for x, y in zip(guitar[i], guitar[j]):
                if x.isdigit():
                    sum1 += int(x)
                if y.isdigit():
                    sum2 += int(y)
            if sum1 > sum2:
                guitar[i], guitar[j] = guitar[j], guitar[i]

            # 3. 사전순 비교
            elif sum1 == sum2:
                for x, y in zip(guitar[i], guitar[j]):
                    if x > y:
                        guitar[i], guitar[j] = guitar[j], guitar[i]
                        break
                    elif x < y:
                        break
for i in range(N):
    for j in range(len(guitar[i])):
        print(guitar[i][j], end='')
    print()