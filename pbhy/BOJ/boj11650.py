# 11650. 좌표 정렬하기
'''
x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬
'''

N = int(input())
arr = []
for i in range(N):
    a, b = map(int, input().split())
    arr.append([a, b])
arr.sort()
for i in arr:
    print(i[0], i[1])