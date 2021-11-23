# 너비 우선 탐색 사용
from collections import deque
def solution(begin, target, words):
    words = [begin] + words
    connection = dict()
    checked = dict()

    # 딕셔너리 생성
    for word in words:
        connection[word] = []
        checked[word] = False
    
    # 그래프 정의
    for i in range(len(words)-1):
        word1 = words[i]
        tmp = words[i+1:].copy()
        while tmp:
            word2 = tmp.pop()
            if is_same(word1,word2):
                connection[word1].append(word2)
                connection[word2].append(word1)
    
    # 너비 우선 탐색 시작
    d = deque([begin])
    dd = deque()
    depth = 0
    while d:
        depth += 1
        while d:
            node = d.popleft()
            checked[node] = True
            for a in connection[node]:
                if a == target:
                    return depth
                if not checked[a]:
                    dd.append(a)
        d = dd
        dd = deque()
    return 0

def is_same(word1,word2):
    n = len(word1)
    ans = 0
    for i in range(n):
        if word1[i] == word2[i]:
            ans +=1
    if ans+1 == n:
        return True
    return False

# b = "hit"
# t = "cog"
# w = ["hot", "dot", "dog", "lot", "log", "cog"]
# print(solution(b,t,w))
