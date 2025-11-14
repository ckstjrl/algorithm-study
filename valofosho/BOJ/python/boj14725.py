"""
BOJ 14725 - 개미굴
문제 정의
1. 로봇 개미는 각 층에 먹이를 따라 내려가다 더 이상 갈 수 없으면 신호
2. 각 층을 따라 N 개의 정보를 제공
3. 로봇 개미가 보내주는 먹이 정보 개수 K가 주어진다.
4. 먹이 이름 길이는 1<=t<=15
5. 먹이 정보는 알파벳 대문자로만 이루어진다
6. 개미굴의 층은 '--'로 구분하며, 같은 층에 여러 방이 있으면 사전 순서가 앞서는 먹이 정보가 먼저 나온다.

로직 정의
1. 우선 이런 문자열과 관련된 문제는 트라이 알고리즘을 통해 해결할 수 있다.(다만 이건 2번 방법으로 할 예정)
2. 우선 모든 정보가 문자열과 길이를 대상으로 정렬을 하고 싶게 한다.-> 정렬 예정

"""

def add(dic, arr):
    if len(arr) == 0:
        return
    # arr 0 번 글자가 dic에 없다면
    if arr[0] not in dic:
       # 이걸 key로 새로 하는 딕셔너리로 채우기
        dic[arr[0]] = {}
    # arr[1:]은 arr[0]을 이미 넣어줬기 때문에 이후부터 재귀
    add(dic[arr[0]], arr[1:])

def printTree(dic, leng):
    for i in sorted(dic.keys()):
        print("--"*leng+i)
        printTree(dic[i], leng+1)


import sys
input = sys.stdin.readline
N = int(input().strip())
arr = [list(map(str, input().split())) for _ in range(N)]
dic = {}

for i in arr:
    # 계층은 빼고
    i = i[1:]
    add(dic, i)

printTree(dic, 0)