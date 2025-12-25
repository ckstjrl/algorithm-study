# 영식 요금제: 30초마다 10원씩 청구 (0 - 29: 10원, 30 - 59: 20원...)

# 민식 요금제: 60초마다 15원씩 청구 (0 - 59: 15원, 60 - 119: 30원...)

Y = 0

M = 0

N = int(input())

usage = list(map(int, input().split()))

for i in usage:
    # 영식 요금제 (30초마다 10원)
    Y = Y + ((i//30) * 10)

    if i % 30 >= 0:
        Y += 10
    
    # 민식 요금제 (60초마다 15원)
    M = M + ((i//60) * 15)

    if i % 60 >= 0:
        M += 15

#최종 금액 비교
if Y > M:
    print(f'M {int(M)}')
elif M > Y:
    print(f'Y {int(Y)}')
else:
    print(f'Y M {int(M)}')