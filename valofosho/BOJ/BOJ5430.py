import sys
import ast
from collections import deque
input=sys.stdin.readline
Tc=int(input())
for i in range (Tc):
    order=str(input())
    num=int(input())
    str_arr=input()
    arr=ast.literal_eval(str_arr)
    de=deque(arr)
    Rcount = 0
    for j in range(len(order)-1):
        if j == (len(order)-2):
            if order[j] == "R":
                Rcount += 1
                if Rcount % 2 == 0:
                    de=str(de)[6:-1].replace(', ',',')
                    print(de)
                    break
                elif Rcount % 2 !=0:
                    de.reverse()
                    de = str(de)[6:-1].replace(', ', ',')
                    print(de)
                    break
            elif order[j] == "D":
                if len(de) == 0:
                    print("error")
                    break
                elif Rcount % 2 == 0:
                    de.popleft()
                    de=str(de)[6:-1].replace(', ',',')
                    print(de)
                    break
                elif Rcount % 2 != 0:
                    de.pop()
                    de.reverse()
                    print(str(de)[6:-1].replace(', ',','))
                    break

        else:
            if order[j] == "R":
                Rcount += 1
            elif order[j] == "D":
                if len(de) == 0:
                    print("error")
                    break
                elif Rcount % 2 == 0:
                    de.popleft()
                elif Rcount % 2 != 0:
                    de.pop()
