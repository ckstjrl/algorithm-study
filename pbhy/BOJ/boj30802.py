# 30802. 웰컴 키트
'''
티셔츠 : S, M, L, XL, XXL, XXXL. 티셔츠는 T장 묶음으로 주문 가능
펜 : 한 종류, P자루씩 묶음으로 주문 or 한 자루씩 주문
티셔츠를 T장씩 최소 몇 묶음 주문해야 하는지, 펜을 P자루씩 최대 몇 묶음 주문할 수 있는지 구해라.

[입력]
첫 줄 : 참가자 수 n
둘째 줄 : S, M, L, XL, XXL, XXXL의 수
셋째 줄 : T, P

[출력]
t 묶음 수
p 묶음 수 낱개 수

t 묶음 수
- `size[i] % t = 0`인 경우 : `size[i] // t`
- `size[i] % t != 0`인 경우 : `(size[i] // t) + 1`

p 묶음 수 : `n // p`
p 낱개 수 : `n % p`
'''
n = int(input())
size = list(map(int, input().split()))
t, p = map(int, input().split())

t_cnt = 0
total_cnt = 0

for i in range(len(size)):
    if (size[i] % t) == 0:
        cnt = size[i] // t
    else:
        cnt = (size[i] // t) + 1
    total_cnt += cnt
print(total_cnt)
print(n // p, n % p)