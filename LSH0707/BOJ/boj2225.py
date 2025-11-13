N, K = map(int, input().split())
# a + b + c + .... + k번째 수 = N (a,b,c,....k >= 0)
# (a+1) + (b+1) + .... + (k번째 수+1) = N+K (a+1,b+1,.... >= 1)
# N+K를 K개로 쪼개기 = (N+K-1) C (K-1)
a = [0,0]  # 분자 [2의갯수, 5의갯수, ....]
b = [0,0]  # 분모 [2의갯수, 5의갯수, ....]
X = N+K-1
y = K-1
for i in range(1, y+1):  # 분자는 (N+K-1 ~~) 분모는 (1,..,K-1)
    x = X
    if x % i == 0:  # 분모분자 나누어 떨어지면
        n = x // i  # 몫
        while n % 2 == 0 or n % 5 == 0:  # 소인수 분해 (2,5) 갯수만 따로 분자에 기록
            if n % 2 == 0:
                n = n // 2
                a[0] = a[0] + 1
            if n % 5 == 0:
                n = n // 5
                a[1] = a[1] + 1
        if n != 1:  # 2,5 제외한 소인수 분자에 append
            a.append(n)
    else:  # 안나누어떨어지면 분자, 분모에 따로 append(2,5 갯수만 따로 나머지는 append)
        while x % 2 == 0 or x % 5 == 0:
            if x % 2 == 0:
                x = x // 2
                a[0] = a[0] + 1
            if x % 5 == 0 :
                x = x // 5
                a[1] = a[1] + 1
        if x != 1:
            a.append(x)
        while i % 2 == 0 or i % 5 == 0:
            if i % 2 == 0:
                i = i // 2
                b[0] = b[0] + 1
            if i % 5 == 0:
                i = i // 5
                b[1] = b[1] + 1
        if i != 1:
            b.append(i)
    X = X - 1
while (a[0] - b[0]) >= 10 and (a[1] - b[1]) >= 10:  # 분모분자 공통된 (2,5)의 갯수 10개씩 빼기
    a[0] = a[0] - 10
    a[1] = a[1] - 10
a[0] = a[0] - b[0]
a[1] = a[1] - b[1]
ans = 2 ** a[0] * 5 ** a[1]
for i in a[2:]:  # 분자
    ans = ans * i
for j in b[2:]:  # 분자 / 분모
    ans = ans // j
print(ans % 1000000000)
