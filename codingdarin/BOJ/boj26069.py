# BOJ 26069. 붙임성 좋은 총총이 (S4 / D2)
n = int(input())

# 댄서 목록 세트 (중복 방지)
dancer = {'ChongChong'}

# 각 만남마다 댄서 추가 조건 체크
for i in range(n):
    a, b = input().split()
    if a in dancer: 
        dancer.add(b)
    elif b in dancer:
        dancer.add(a)
        
print(len(dancer)) 
        
