
def solution(s):
    l = len(s)
    ans = l
    for cut in range(int(l/2)):
        cut +=1
        comp_s = s
        target = comp_s[0:cut]
        # comp_s = comp_s[:-cut]
        # print([cut,target, comp_s])
        i = cut
        new_ans = l
        num_compressing = 0
        while i + cut <= l:
            if target == comp_s[i:i+cut]:
                if num_compressing == 0:
                    new_ans += 1
                else:
                    if num_compressing == 8:
                        new_ans +=1
                    if num_compressing == 98:
                        new_ans +=1
                    if num_compressing == 998:
                        new_ans +=1
                new_ans -= cut
                num_compressing +=1
            else:
                num_compressing = 0
                target = comp_s[i:i+cut]
            i += cut
        # print([cut,target,new_ans])
        if ans > new_ans:
            ans = new_ans
    return ans

solution("xxxxxxxxxxyyy")
# print("abcde"[1:3])

# abc abc
# 012 345