# BOJ27160 할리갈리

# 가능한 모든 과일 옵션
fruits = {
    'STRAWBERRY': 0,
    'BANANA': 0,
    'LIME': 0,
    'PLUM': 0,
}

# 몇 번에 걸쳐서 카드를 뽑을지
N = int(input())

# 들어오는 카드의 숫자만큼 해당 과일의 val을 높여주기
for i in range(N):
    fruit, num = input().split()

    if fruit in fruits:
        fruits[fruit] += int(num)

# 5가 된 과일이 있는지 딕셔너리를 확인하고 있으면 YES 아니면 NO
if 5 in fruits.values():
    print('YES')
else:
    print('NO')





