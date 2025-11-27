'''
BOJ9935 / D3): 문자열 폭발

해결 방법 : 
1. 모든 단어들을 하나씩 stack에 옮기기
2. 만약, stack의 길이가 bomb보다 같거나 긴 경우,
3. bomb의 길이만큼 뒤에서부터 stack과 bomb의 단어들이 같은지 확인하기
4. 하나라도 다르면 flag를 통해 skip
5. bomb 길이만큼 같다면, bomb 길이만큼 stack에서 pop하기
'''

pre_explode = list(input())
bomb = list(input())

stack = []
for word in pre_explode:
    stack.append(word)
    flag = True
    if len(stack) >= len(bomb):
        for i in range(-1, -(len(bomb))-1, -1):
            if stack[i] == bomb[i]:
                continue
            else:
                flag = False
                break
        if flag == True:
            for _ in range(len(bomb)):
                stack.pop()

if stack:
    print(''.join(stack))
else:
    print("FRULA")
