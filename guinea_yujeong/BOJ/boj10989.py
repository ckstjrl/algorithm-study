# 10989 수 정렬하기 

#오름차순 sort 함수 활용 
'''
1차 시도 (땡!)
n = int(input())

print(sorted(n))
'''

# 계수정렬(counting sort)을 써야한다고 함
import sys
n = int(sys.stdin.readline())

counting = [0]*10000

for i in range(n):
    a = int(sys.stdin.readline())
    counting[a-1] += 1
for x in range(10000):
    if counting[x] !=0:
        for j in range(counting[x]):
            print(x+1)  
