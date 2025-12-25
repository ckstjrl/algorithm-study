"""
한 번호가 다른 번호의 접두어인 경우는 없어야 한다

"""
class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        cur_node = self.head
        for char in string:
            if char not in cur_node.children:
                cur_node.children[char] = Node(char)
            cur_node = cur_node.children[char]
            # 만약 도중에 이미 끝나는 번호가 있으면 (다른 번호가 prefix)
            if cur_node.data is not None:
                return False
        # 삽입 끝났는데 이미 하위 노드가 있으면 (내 번호가 prefix)
        if cur_node.children:
            return False
        cur_node.data = string
        return True


import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    numbers = [input().strip() for _ in range(N)]
    numbers.sort()  # 정렬하면 앞 번호가 뒤 번호의 prefix인지 쉽게 확인 가능

    trie = Trie()
    is_consistent = True
    for num in numbers:
        if not trie.insert(num):
            is_consistent = False
            break

    print("YES" if is_consistent else "NO")








"""
Trie 안쓰고 Sorting으로 풀이
"""
# import sys
# input = sys.stdin.readline
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     arr = []
#     for i in range(N):
#         num = input().strip()
#         arr.append(num)
#     # 문자열에서 숫자 sorting을 활용
#     # 문자열에서는 길이가 우선이 아닙니다
#     arr.sort()
#     for i in range(len(arr)-1):
#         if arr[i+1].startswith(arr[i]):
#             print('NO')
#             break
#     else:
#         print('YES')
