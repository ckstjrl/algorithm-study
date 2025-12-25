# 2447. 별 찍기 - 10

N = int(input())
k = 0   # 3**k = N인 k 
while 3**k < N:
    k += 1

# 규칙: 
# 이번 (N) 패턴은 이전 (N/3) 패턴을 가운데를 비우고 나머지 8칸에 채우는 것
# [O][O][O]
# [O]---[O]
# [O][O][O]
# 이렇게 생겼으므로 [3번 반복] + [한번 + 비우고 + 한번] + [3번 반복] 으로 생성

def make_pattern(k):
    base = ['***', '* *', '***']
    p = base
    for i in range(1, k):
        space = ' ' * (3**i)
        p =[x*3 for x in p] + [x + space + x for x in p] + [x*3 for x in p]     # 이번 패턴 찾기
    return p

result = make_pattern(k)
print(*result, sep='\n')    # 출력 