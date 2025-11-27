'''
27160번 할리갈리 

[문제]
게임초보 한별이가 이길 수 있도록 할리갈리 요정이 되어보자 

[입력]
첫 번째 줄에 펼쳐진 카드의 개수 N이 주어집니다.
두 번째 줄부터 N개의 줄에 걸쳐 한 줄에 하나씩 펼쳐진 카드의 정보가 주어집니다.
카드의 정보는 공백으로 구분된, 과일의 종류를 나타내는 문자열 S와 과일의 개수를 나타내는 양의 정수 X로 이루어져 있습니다. 

S는 strawberry, BANANA, LIME, PLUM 중 하나입니다. 
'''

N = int(input())  # 펼쳐진 카드의 개수 

# 과일 개수를 저장하기
fruit_num = {
    'STRAWBERRY': 0,
    'BANANA': 0,
    'LIME': 0,
    'PLUM': 0,
}

for i in range(1,N+1):
    card, number = input().split() # 카드의 정보
    number = int(number)
    fruit_num[card] += number # 같은 과일끼리 개수 더하기
    #  같은 과일이고 숫자가 5와 같은지 확인
bell = 'NO'
for fruit in fruit_num:
    if fruit_num[fruit] == 5:
        bell = 'YES'
        break
print(bell)