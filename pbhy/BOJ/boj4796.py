# 4796. 캠핑
'''
캠핑장을 연속하는 P일 중, L일동안만 사용할 수 있다.
강산이는 이제 막 V일짜리 휴가를 시작했다.
강산이가 캠핑장을 최대 며칠동안 사용할 수 있을까? (1 < L < P < V)

테스트케이스의 수가 나오지 않으니까 while문을 돌려야 함.
먼저 l, p, v 가 모두 0일 때부터 해서 계산을 줄이자.
'''
tc = 1
while True:
    l, p, v = map(int, input().split())
    if l == 0 and p == 0 and v == 0:
        break
    else:
        result = (v // p) * l
        if l > v % p:
            result += v % p
        else:
            result += l
    print(f'case {tc}: {result}')
    tc += 1