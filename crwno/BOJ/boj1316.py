N = int(input())

res = 0

for _ in range(N):
    check = input()
    check_rev = [check[0]]
    visited = [False] * 26
    for i in range(1, len(check)):
        if check_rev[-1] != check[i]:
            check_rev.append(check[i])
    for i in range(len(check_rev)):
        if not visited[ord(check_rev[i]) - 97]:
            visited[ord(check_rev[i]) - 97] = True
        else:
            res += 1
            break
ans = N - res
print(ans)
