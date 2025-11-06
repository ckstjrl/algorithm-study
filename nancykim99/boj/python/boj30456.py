'''
BOJ30456 / D1): 바닥수 (B1)

해결방법 : 어차피 곱셈이니, 마지막 숫자를 n으로 채우고 나머지 1로 채우기
>> 문제가 이상해요
'''

n, l = map(int, input().split())

arr = []
for i in range(l-1):
    arr.append('1')

arr.append(str(n)) 

print(''.join(arr))