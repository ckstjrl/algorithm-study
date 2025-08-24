def s_push(s, x):
    s.append(x)
    return s
def s_pop(s):
    if s:
        print(s[-1])
        s.pop()
        return s
    else:
        print(-1)
        return s
def s_size(s):
    s_len=len(s)
    print(s_len)
    return s

def s_empty(s):
    if not s:
        print(1)
        return s
    if s:
        print(0)
        return s
def s_top(s):
    if not s:
        print(-1)
        return s
    else:
        print(s[-1])
        return s
import sys
input=sys.stdin.readline
N=int(input())
s=[]
for i in range(N):
    op=input().split()
    if "push" in op:
        x=op[1]
        s=s_push(s,x)
    elif "pop" in op:
        s=s_pop(s)
    elif "size" in op:
        s=s_size(s)
    elif "empty" in op:
        s=s_empty(s)
    elif "top" in op:
        s=s_top(s)