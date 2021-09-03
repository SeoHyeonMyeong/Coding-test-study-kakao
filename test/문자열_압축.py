
def solution(s):
    l = len(s)
    ans = l
    for cut in range(int(l/2)):
        cut +=1
        comp_s = s
        target = comp_s[-cut:]
        # comp_s = comp_s[:-cut]
        # print([cut,target, comp_s])
        i = l -1 -cut
        new_ans = l
        isCompressing = False
        while i >= cut-1:
            if target == comp_s[i+1-cut:i+1]:
                i -= cut
                if isCompressing:
                    new_ans -= cut    
                else:
                    new_ans += 1
                    new_ans -= cut
                    isCompressing = True
            else:
                isCompressing = False
                i += cut - 1
                target = comp_s[i+1-cut:i+1]
                i -= cut
        print([cut,target,new_ans])
    #     if ans > new_ans:
    #         ans = new_ans
    # return ans

solution("xababcdcdababcdcd")
# print("abcde"[1:3])

# abc abc
# 012 345