def solution(s):
    tmp = []
    for i in range(len(s)):
        if i < len(s)-1 and s[i] == s[i+1]:
            tmp.append([s[i]*2 , i, i+1])
        tmp.append([s[i],i,i])

    ans = 1
    while tmp:
        print(tmp)
        str_, start, end = tmp.pop()
        if start == 0 or end == len(s)-1:
            length =  end - start + 1
            ans = max(ans,length)
        else:
            if s[start-1] == s[end+1]:
                c = s[end+1]
                tmp.append([c+str_+c,start-1,end+1])
            else:
                length = end - start + 1
                ans = max(ans,length)
    return ans
#palindrome
s = "abbba"
print(solution(s))