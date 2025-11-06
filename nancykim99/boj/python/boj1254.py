'''
BOJ1254 / D2): 팰린드롬 만들기

해결 방법 :
1. 기준점을 옮기면서 팰린드롬인지 확인 -> 기준을 옮기는게 번거로워서 포기.
짝수면 반+1, 홀수면 반을 기준으로 팰린드롬인지 확인
    1) 팰린드롬이면, `len(arr)`이 min 팰린드롬
    2-1) 아닐 시, 짝수라면 기준을 중심으로 양쪽을 비교하면서 다를때까지 확인
        3-1) 끝까지 갔는데, 다 같다면, 앞쪽보다 부족한 부분을 추가한다고 생각하고 `len(arr) + 부족한 len`이 min 팰린드롬
        3-2) 끝까지 가기 전에, 다른 부분이 나타난다면, 기준을 + 1해서 다시 확인
    2-2) 홀수라면, 기준을 + 1해서 양쪽 비교하기 (짝수랑 똑같이 진행)

2. 어차피 팰린드롬이라면, 하나씩 줄여나가면서 뒷부분을 확인하고, 팰린드롬이 만들어지면, 줄인 부분만 추가하면 됨
    1) 슬라이싱하면서, -1하면서 뒷부분이 팰린드롬인지 확인
    2-1) 뒷부분이 짝수라면, j까지 앞부분, j부터 뒷부분
    2-2) 뒷부분이 홀수라면, j-1까지 앞부분, j+1부터 뒷부분
'''

arr = list(input())
n = len(arr)
ans = 0

for i in range(n):
    is_palindrome = False
    arr_pre = arr[i:]
    mid = len(arr_pre) // 2
    if len(arr_pre) % 2 == 0:
        front = arr_pre[:mid]
        back = arr_pre[mid:]
        if front == back[::-1]:
            is_palindrome = True
    if len(arr_pre) % 2 == 1:
        front = arr_pre[:mid]
        back = arr_pre[mid+1:]
        if front == back[::-1]:
            is_palindrome = True
    
    if is_palindrome:
        ans = n + i
        break

print(ans)