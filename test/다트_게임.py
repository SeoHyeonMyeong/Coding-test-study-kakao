def solution(dartResult):
    arr = []
    pop = ""
    while len(dartResult) > 0:
        pop += dartResult[0]
        dartResult= dartResult[1:]
        
        if len(dartResult) == 0:
            arr.append(pop)
            continue
        if pop.isnumeric() and dartResult[0].isnumeric():
            continue
        elif dartResult[0].isnumeric():
            arr.append(pop)
            pop = ""
    
    ans = []
    for str in arr:
        if str[0:2].isnumeric():
            ans.append(int(str[0:2]))
        else:
            ans.append(int(str[0]))

    for i in range(len(arr)):
        if "S" in arr[i]:
            ans[i] **= 1
        elif "D" in arr[i]:
            ans[i] **= 2
        elif "T" in arr[i]:
            ans[i] **= 3
        
        if '*' in arr[i]:
            if i == 0:
                ans[i] *= 2
            else:
                ans[i] *= 2
                ans[i-1] *=2

        if '#' in arr[i]:
            ans[i] *= -1
    
    return sum([i for i in ans])

print(solution("10D10S10S"))