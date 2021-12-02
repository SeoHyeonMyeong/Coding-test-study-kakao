def solution(user_id, banned_id):
    tmp = []
    for ban in banned_id:
        lst = []
        for user in user_id:
            if comp(user,ban):
                lst.append(user)
        tmp.append(lst)
    ans = [[]]
    new = []
    while tmp:
        a = tmp.pop()
        for item in a:
            for arr in ans:
                arr_ = arr.copy()
                if not item in arr_:
                    arr_.append(item)
                    arr_.sort()
                    if not arr_ in new:
                        new.append(arr_)
        ans = new
        new = []
    return len(ans)

def comp(id1,id2):
    if len(id1) != len(id2):
        return False
    for i in range(len(id1)):
        a = id1[i]
        b = id2[i]
        if a == "*" or b == "*":
            continue
        if a!=b:
            return False
    return True
