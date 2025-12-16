# BOJ 5567. 결혼식 / D2
'''
문제
상근이는 자신의 결혼식에 학교 동기 중 자신의 친구와 친구의 친구를 초대하기로 했다.
상근이의 동기는 모두 N명이고, 이 학생들의 학번은 모두 1부터 N까지이다. 상근이의 학번은 1이다.

상근이는 동기들의 친구 관계를 모두 조사한 리스트를 가지고 있다.
이 리스트를 바탕으로 결혼식에 초대할 사람의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 상근이의 동기의 수 n (2 ≤ n ≤ 500)이 주어진다.
둘째 줄에는 리스트의 길이 m (1 ≤ m ≤ 10000)이 주어진다.
다음 줄부터 m개 줄에는 친구 관계 ai bi가 주어진다. (1 ≤ ai < bi ≤ n) ai와 bi가 친구라는 뜻이며, bi와 ai도 친구관계이다.

출력
첫째 줄에 상근이의 결혼식에 초대하는 동기의 수를 출력한다.
'''
import sys
from collections import deque

input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

f = []

q = deque(graph[1])
while q:
    a = q.popleft()
    f.append(a)
    for i in graph[a]:
        if i != 1:
            f.append(i)

invite = set(f)
print(len(invite))

'''
친구의 친구까지만 부른다
q에 상근이의 친구를 넣는다
while문을 통해서 q에서 하나씩 뽑아서
친구를 f에 넣고 친구의 친구가 1이 아닌 경우 f에 넣어준다 (1을 빼는 이유는 상근이 본인이니까)
이후 친구들의 중복을 없애기 위해
invite 변수를 만들고 set으로 처리
invite의 길이 = 초대할 사람의 수
'''