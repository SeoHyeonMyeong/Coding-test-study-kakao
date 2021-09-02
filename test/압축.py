dic = []
for i in range(ord('A'), ord('Z')+1):
    dic.append(chr(i))

def solution(msg):
    global dic
    ans = []
    i = 0
    while i < len(msg):
        n = len(msg)
        word = msg[i:n]
        while not word in dic:
            n -= 1
            word = msg[i:n]
        ans.append(dic.index(word) + 1)
        if not i == len(msg)-1:
            dic.append(msg[i:n+1])
        i = n
    print(ans)
    return ans