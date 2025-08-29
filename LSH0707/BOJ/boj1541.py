arr = list(map(str, input().split('-')))  # 최솟값을 만들기위해 '-'기준으로 자르고 0번인덱스에서 남은 모든수를 빼기
def cal(char):
    lst = list(map(str, char.split('+'))) # [a, b+c, d+e+f ~~~~~] --> [A, B, C, ~~~~~]
    ans = 0
    for i in lst:
        ans = ans + int(i)
    return ans
result = cal(arr[0])  # 0번 숫자
for i in range(1, len(arr)):  # [A, B, C,~~~~~] --> A-B-C-~~~~~~
    result = result - cal(arr[i])
print(result)
    

