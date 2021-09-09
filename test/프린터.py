def solution(priorities, location):
    prior_set = list(set(priorities))
    prior_set.sort(reverse=True)
    print(prior_set)
    count = 1
    
    for p in prior_set:
        while p in priorities:
            i = priorities.index(p)
            if i == location:
                return count
            else:
                priorities = priorities[i+1:] + priorities[:i]
                if location > i:
                    location -= i+1
                else:
                    location += len(priorities) - i
                count += 1
    return count

pr = [1,1,3,6,1,1,1,1,9,1,1,1]
lo = 2
print(solution(pr,lo))