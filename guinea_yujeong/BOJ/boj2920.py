#백준 2920.음계
'''
a = list(map(int, input().split()))

if a ==[1, 2, 3, 4, 5, 6, 7, 8]:
    print('ascending')
elif a ==[8, 7, 6, 5, 4, 3, 2, 1]:
    print('descending')
else : 
    print('mixed')

'''

a = list(map(int, input().split())) 

if a == sorted(a): #오름차순 함수 sorted(리스트명)
    print('ascending')
elif a == sorted(a, reverse=True): #내림차순 sorted(리스트명, reverse=True)
    print('descending')
else : 
    print('mixed')