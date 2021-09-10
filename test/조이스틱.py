def solution(name):
    li = []
    cursor = 0
    ans = 0

    for char in name:
        num = ord(char) - ord("A")
        if 26 - num < num:
            num = 26-num
        li.append(num)
    
    i,pos = 0,0
    while i != -1:
        ans += pos
        ans += li[i]
        li[i] = 0
        cursor = i
        i,pos = find_near(li,cursor)

    return ans

def find_near(li,cursor):
    n = len(li)
    near = 1000
    near_i = -1
    for i in range(n):
        pos = abs(cursor - i)
        if n - pos < pos:
            pos = n-pos
        if pos<near and li[i] != 0:
            near = pos
            near_i = i
    return near_i, near

name = "JEROEN"
print(solution(name))