def solution(n):
    # 배열 만들기
    ans = []
    for i in range(n):
        ans.append([0]*(i+1))

    # 진행방향 3방향
    # [1, 0] [0, 1] [-1,-1]
    directions = [[1,0],[0,1],[-1,-1]]

    row, col = -1,0
    d = 2
    num = 0

    while n > 0:
        d = {0:1,1:2,2:0}.get(d)
        move = directions[d]
        for i in range(n):
            num += 1
            row += move[0]
            col += move[1]
            ans[row][col] = num
        n -= 1
    return sum(ans,[])


# n = 4
# print(solution(n))


'''
1
2 12 
3 13 11 
4 14 15 10
5  6  7  8  9 

[1,2,9,3,10,8,4,5,6,7]
[1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]
[1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]
'''