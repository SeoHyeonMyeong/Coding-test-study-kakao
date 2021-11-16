from collections import deque

def solution(enroll, referral, seller, amount):
    
    n = len(enroll)

    # parent 딕셔러니 생성
    parent = dict()
    for i in range(n):
        parent[enroll[i]] = referral[i]

    # child 딕셔너리 생성
    child = dict()
    for person in enroll:
        child[person] = 0
    for i in range(n):
        if referral[i] == "-":
            pass
        else:
            child[referral[i]] +=1

    # result 딕셔너리 생성
    result = dict()
    for person in enroll:
        result[person] = 0
    
    # 벌어들인 돈 계산
    for i in range(len(seller)):
        person = seller[i]
        parent_ = parent[person]
        money = amount[i] * 100
        fee = money // 10
        while True:
            if money == 0:
                break
            result[person] += money - fee
            if parent_ == "-":
                break
            money = fee
            fee = money //10
            person = parent_
            parent_ = parent[person]

    # # 다단계 수행
    # tmp = deque(enroll.copy())
    # while tmp:
    #     person = tmp.popleft()
    #     if child[person] != 0:
    #         tmp.append(person)
    #     else:
    #         tax = result[person] // 10
    #         result[person] -= tax
    #         if not parent[person] == "-":
    #             result[parent[person]] += tax
    #             child[parent[person]] -= 1

    return list(result.values())



# e = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
# r = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
# s = ["young", "john", "tod", "emily", "mary"]
# a = [12, 4, 2, 5, 10]
# print(solution(e,r,s,a))