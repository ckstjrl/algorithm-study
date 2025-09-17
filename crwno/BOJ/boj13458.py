N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
ans = 0
# 총감독관 일단 N명
ans += N
# 커버안되는거 추가하기
for i in range(N):
    if A[i] - B > 0:
        ans += ((A[i] - B) // C)
        if (A[i] - B) % C != 0:
            ans += 1
print(ans)