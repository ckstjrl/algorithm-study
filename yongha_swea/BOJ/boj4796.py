# BOJ 4796 캠핑

cont = True

tc = 0

while cont:

    ans = 0

    tc += 1

    P, L, V = map(int, input().split())

    if P == 0 and L == 0 and V == 0:
        break
    
    #온전히 사용 가능한 날 (L일 중 P일)
    ans = ans + (P * (V // L))

    #나머지 일 수

    #나머지가 연속 사용 가능일수보다 작거나 같은 경우 (전부 사용 가능)
    if (V % L) <= P:
        ans = ans + (V % L)
    else:
        ans = ans + P

    print(f'Case {tc}: {ans}')    