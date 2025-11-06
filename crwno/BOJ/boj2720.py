T = int(input())
for tc in range(1, T + 1):
    C = int(input())
    ans = [0, 0, 0, 0]
    if C >= 25:
        ans[0] += C // 25
        C = C % 25
    if C >= 10:
        ans[1] += C // 10
        C = C % 10
    if C >= 5:
        ans[2] += C // 5
        C = C % 5
    if C >= 1:
        ans[3] += C
        C = 0
    print(*ans)
    #언패킹하기 **********