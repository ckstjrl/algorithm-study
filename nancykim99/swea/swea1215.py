T = int(input())
 
for tc in range(1, T+1):
    N, M = map(int,input().split())
    txt = [list(input()) for _ in range(N)]
    result = ''
    for i in range(N):
        for s in range(N-M+1):
            ans = txt[i][s:s+M]
            if ans[:M//2] == ans[-(M//2):][::-1]:
                result = ''.join(ans)
    for j in range(N):
        default = []
        for i in range(N):
            default.append(txt[i][j])
        for s in range(N-M+1):
            ans = default[s:s+M]
            if ans[:M//2] == ans[-(M//2):][::-1]:
                result = ''.join(ans)
    print(f'#{tc} {result}')


