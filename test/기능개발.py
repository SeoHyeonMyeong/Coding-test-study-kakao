def solution(progresses, speeds):
    n = len(progresses)
    ans = []
    i = 0
    while i<n:
        day_need = (100 - progresses[i]) / speeds[i]
        if day_need <= 0:
            i += 1
            ans[-1] += 1
            continue
        if int(day_need) == day_need:
            day_need = int(day_need)
        else:
            day_need = int(day_need)+1
        for j in range(i,n):
            progresses[j] += day_need * speeds[j]
        i += 1
        ans.append(1)
    return ans



p = [93, 30, 55]
s = [1, 30, 5]
print(solution(p,s))