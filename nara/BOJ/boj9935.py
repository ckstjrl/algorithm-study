import sys
input = sys.stdin.readline

string = input().strip()
word = input().strip()

def check_word(string):
    stack = []
    top = -1
    for x in string:
        stack.append(x)
        top += 1
        if stack[top] == word[-1]:
            if word == ''.join(stack[top-len(word)+1:top+1]):
                for _ in range(len(word)):
                    stack.pop()
                    top -= 1
    return stack

ans = check_word(string)
if ans:
    print(''.join(ans))
else:
    print('FRULA')