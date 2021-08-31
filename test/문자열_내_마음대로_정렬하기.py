def solution(strings, n):
    ans = []

    for s in strings:
        ans.append([ord(s[n]),s])

    ans.sort(key=lambda x:(x[0],x[1]))
    num,ans = zip(*ans)
        
    return ans
print(solution(["sun","bed","car","aar"],1))