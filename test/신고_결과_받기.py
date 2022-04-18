user = dict()

def solution(id_list, report, k):
    global user
    ans = []
    reported = []
    for i in id_list:
        user[i] = [[],0]
    for rep in report:
        rep = rep.split(" ")
        user_1 = user[rep[0]]
        user_2 = rep[1]
        if not user_2 in user_1[0]:
            user_1[0].append(user_2)
            user[user_2][1] += 1
    for u in user.keys():
        if user[u][1]>=k:
            reported.append(u)
    for u in user.keys():
        sum = 0
        for r in user[u][0]:
            if r in reported:
                sum +=1
        ans.append(sum)
    return ans


# id_list = ["muzi", "frodo", "apeach", "neo"]
# report = ["muzi frodo","muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
# k = 2

# print(solution(id_list,report,k))