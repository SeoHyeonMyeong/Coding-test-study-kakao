def solution(a):
    if len(a) < 2 :
        return 0

    count = dict()
    indices = dict()

    for i in range(len(a)):
        num = a[i]
        if num in count:
            count[num] += 1
            indices[num].append(i)
        else:
            count[num] = 1
            indices[num] = [i]

    lst = []
    for i in range(len(count)):
        lst.append([list(count.keys())[i],list(count.values())[i]])
    lst.sort(key = lambda x: x[1])

    print(lst)
    ans = 0

    while lst:
        num, count= lst.pop()
        panalty = 0

        count *= 2

        if count < ans:
            return ans
        
        tmp = indices[num]
        for i in range(len(tmp)):
            if i == 0:
                left = -1
            else:
                left = tmp[i-1]

            if i == len(tmp)-1:
                right = len(a)
            else:
                right = tmp[i+1]
            
            mid = tmp[i]
            dist = right - left -2 - panalty
            if dist >= 1:
                if dist == 1 and right - mid -1 == 1:
                    panalty = 1
                else:
                    panalty = 0
                continue
            count -= 2

        ans = max(ans,count)
        

    return indices[num]


a = [0]                     # 0
a = [5,2,3,3,5,3]           # 4
# a = [0,3,3,0,7,2,0,2,2,0]   # 8

print(solution(a))


313