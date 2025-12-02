'''
BOJ17298 : 오큰수 (G4)

해결 방법 :
1. n-2부터 다음 숫자와 비교해서 더 크면, ans와 temp에 넣기
2. 같거나 작은 경우, temp[-1]와 비교해서 temp가 큰 경우 ans
3. temp[-1]와도 같거나 작은 경우, temp 업데이트 (temp[-1]가 더 클때까지 pop) 및 ans는 -1
'''
import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
temp = []
ans = [-1]

for i in range((n-2), -1, -1):
    if arr[i+1] > arr[i]:
        ans.append(arr[i+1])
        temp.append(arr[i+1])
    else:
        if temp[-1] > arr[i]:
            ans.append(temp[-1])
        else:
            while temp[-1] <= arr[i] and temp[-1] != -1:
                temp.pop()
            if temp[-1] > arr[i]:
                ans.append(temp[-1])
            else:
                ans.append(-1)

ans.reverse()
print(*ans)