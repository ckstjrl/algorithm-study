#BOJ2355 시그마

A, B = map(int, input().split())

#A가 B보다 큰 경우 서로 위치를 바꿔준다
if A > B:
    A, B = B, A

ans = 0

# #이 코드의 문제는 큰 범위에 대해서 반복문을 돌리니 시간 제한을 야기한다
# for i in range(A, B+1):
#     ans += i

#수학적인 접근법을 사용해야 한다, 등차수열의 합공식을 활용

# A부터 B까지의 합 = (A + B) × (B - A + 1) / 2

ans = (A + B) * (B - A + 1) // 2

print(ans)