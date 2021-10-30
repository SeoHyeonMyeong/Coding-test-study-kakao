def solution(n, words):
    i = wrong_index(words)
    if i == 0:
        return [0,0]
    a = i % n +1
    b = int(i / n) +1
    return [a,b]

def wrong_index(words):
    l = []
    last = words[0][0]
    for i in range(len(words)):
        word = words[i]
        if word[0] != last:
            return i
        if word in l:
            return i
        l.append(word)
        last = word[-1]
    return 0

# n = 5
# word = 	["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]
# print(solution(n,word))