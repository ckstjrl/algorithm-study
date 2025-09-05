T = int(input())
for tc in range(1, T + 1):
    R, S = map(str, input().split())
    R = int(R)
    res = ''
    for i in range(len(S)):
        res += S[i] * R
    print(res)