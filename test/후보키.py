import numpy as np
def solution(relation):
    # 컬럼으로 배열을 쪼갠다
    relation = np.array(relation).T.tolist()

    # 초기 타겟은 모든 col을 포함한 키
    targets = [[i for i in range(len(relation))]]
    # lst = []
    # for i in targets[0]:
    #     if len(lst) ==0:
    #         lst = relation[i].copy()
    #     else:
    #         lst = [x+y for x,y in zip(lst,relation[i])]
    # print(lst)
    # if not is_candidate(lst):
    #     return 0
    print(targets)
    ans = []

    # 모든 타겟의 candidate 체크
    while targets:
        check = 0
        tmp = targets.pop(0)
        # 해당 타겟에서 키를 하나씩 제외했을때 유일성을 만족하는지 체크
        for i in range(len(tmp)):
            a = tmp.copy()
            a.remove(tmp[i])
            lst = []
            # 키 하나를 제거한 a 배열의 데이터를 만들어 lst에 저장
            for j in a:
                if len(lst) == 0:
                    lst = relation[j].copy()
                else:
                    lst = [x+" "+y for x,y in zip(lst,relation[j])]
            # lst가 비어있다면
            if len(lst) == 0:
                ans.append(tmp)
            # lst가 유일성을 만족하고 타겟에 없다면 타겟에 추가
            elif (is_candidate(lst)) and (a not in targets):
                targets.append(a)
            # lst가 유일성을 만족하지 않을경우 check ++
            elif not is_candidate(lst):
                check += 1
        # 모든 하위 항목이 유일성을 만족하지 않았을 경우 정답에 추가
        if check == len(tmp):
            ans.append(tmp)
    return len(ans)

def is_candidate(arr):
    if len(arr) == len(set(arr)):
        return True
    return False

# data = [["aa","bb"],["cc","dd"]]
# data = [["a","1","aaa","c","ng"],["a","1","bbb","e","g"], ["c","1","aaa","d","ng"], ["d","2","bbb","d","ng"]]
# print(solution(data))