def solution(begin, target, words):
    ans = []
    for word in words:
        if is_same(begin,word):
            ans.append(word)
    return ans

def is_same(word1,word2):
    n = len(word1)
    ans = 0
    for i in range(n):
        if word1[i] == word2[i]:
            ans +=1
    if ans+1 == n:
        return True
    return False

b = "hit"
t = "cog"
w = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(b,t,w))