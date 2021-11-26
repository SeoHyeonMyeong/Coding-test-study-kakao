def solution(routes):
    routes.sort(key=lambda x: x[1])
    end = -30001
    ans = 0
    for a,b in routes:
        if a <= end:
            pass
        else:
            end = b
            ans +=1
    return ans

# r = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
# print(solution(r))