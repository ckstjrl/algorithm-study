'''
백준 1764 듣보잡

듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.
[입력]
첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어진다. 이어서 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과, N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다. 이름은 띄어쓰기 없이 알파벳 소문자로만 이루어지며, 그 길이는 20 이하이다. N, M은 500,000 이하의 자연수이다.

듣도 못한 사람의 명단에는 중복되는 이름이 없으며, 보도 못한 사람의 명단도 마찬가지이다.
[출력]
듣보잡의 수와 그 명단을 사전순으로 출력한다.
'''

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

list = set()   # 명단 입력
for i in range(N):
    list.add(input().strip())

result = []      # 명단 목록 저장
for x in range(M):
    name = input().strip()
    if name in list:
        result.append(name)

result.sort() #정렬

print(len(result))
for name in result:
    print(name)


