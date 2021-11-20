def solution(n, results):
    wins = [[] for i in range(n+1)]
    loses = [[] for i in range(n+1)]
    tmp = []
    rate = [0,n+1]
    ans = 0

    # 모든 결과 처리
    for a in results:
        win, lose = a
        wins[win].append(lose)
        loses[lose].append(win)

    # winer와 loser의 숫자 세기
    for i in range(n):
        winer = wins[i]
        temp = winer.copy()
        while temp:
            t = temp.pop(0)
            arr = wins[t]
            for j in arr:
                if j not in winer:
                    winer.append(j)
                    temp.append(j)

        loser = loses[i]
        temp = loser.copy()
        while temp:
            t = temp.pop(0)
            arr = loses[t]
            for j in arr:
                if j not in loser:
                    loser.append(j)
                    temp.append(j)
        count = len(winer) + len(loser)

        if count == n-1:
            tmp.append(i)
            rate.append(len(loser)+1)

    rate.sort()
    right = 0
    while rate:
        left = right
        right = rate.pop(0)
        if right - left == 2:
            ans += 1
        ans += 1
    return ans - 2

# n = 4
# results = [[1, 2], [2, 3], [1, 4]]
# print(solution(n,results))