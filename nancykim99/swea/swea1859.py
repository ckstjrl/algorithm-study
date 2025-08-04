# 문제 해결 방법 :
# input 받은 숫자들을 작은 숫자에 사서 큰 숫자에 팔아야 함
# a, b, c, d, e 라고 했을 때,
# a, b를 비교하고, b가 크면, b와 c를 비교, c가 크면, c와 d를 비교 등
# 만약 c와 d를 비교했는데, c가 크면, c - b, c - a 등 하고 차들을 전부 sum

T = int(input()) # 테스트 케이스

for tc in range(1, T+1):
    value_num = int(input())
    list_of_num = list(map(int, input().split()))

    a = list_of_num[0]
    b = 0
    c = []
    d = 0

    for i in range(value_num):
        if a < list_of_num[i]: # 만약 [0] 보다 큰 경우
            a = list_of_num[i] # a에 추가
            b += 1 # 인덱스를 알아내기 위해 1 추가
        elif a >= list_of_num[i]: # 만약 a보다 다음 숫자가 큰 경우
            for i in range(b): 
                c += [list_of_num[b] - list_of_num[i]] # 차들을 c리스트에 추가
                d += 1

    
    e = 0
    for i in range(d):
        e += c[i]   

    print(f'#{tc}', e)

# 어딘가에서 값을 못 받고 있다...!!!
# 계속 0만 나옴