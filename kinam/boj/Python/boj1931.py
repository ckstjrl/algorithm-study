'''boj1931 회의실 배정
한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다. 
각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자. 
단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다. 
회의의 시작시간과 끝나는 시간이 같을 수도 있다. 
이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.
'''
from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
#끝나는 시간이 빠른 순으로 정렬, 끝나는 시간이 같다면 시작 시작이 빠른 순으로 정렬
arr.sort(key=lambda x:(x[1], x[0]))
cnt = 1
ni = 0

for i in range(1, len(arr)):
    if arr[ni][1] > arr[i][0]: #이전회의 끝나는 시간이 다음회의의 시작시간보다 크면 다음회의는 시작 못함
        continue
    else:
        ni = i
        cnt += 1
print(cnt)
