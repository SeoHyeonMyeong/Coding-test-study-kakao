def solution(n,a,b):
    ans = 0
    
    a-=1
    b-=1
    while a != b:
        ans += 1
        a = int(a/2)
        b = int(b/2)

    return ans

n = 8
a = 4
b = 7

print(solution(n,a,b))