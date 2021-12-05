from collections import deque

count = dict
def solution(gems):
    # 보석 개수 세기
    count = dict()
    for gem in gems:
        if gem in count:
            count[gem] +=1
        else:
            count[gem] = 1

    gems = deque(gems)
    start = 1
    end = len(gems)
    # 뒤부터 보석 하나씩 제거    
    while True:
        gem = gems.pop()
        if count[gem] == 1:
            gems.append(gem)
            break
        else:
            end -= 1
            count[gem] -= 1
    # 앞부터 보석 하나씩 제거
    while True:
        gem = gems.popleft()
        if count[gem] == 1:
            return [start,end]
        else:
            start += 1
            count[gem] -= 1

def dfs(gems):


# g = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]     # 3,7
# g = ["AA", "AB", "AC", "AA", "AC"]      # 1,3
# g = ["XYZ", "XYZ", "XYZ"]       #  1,1
# g = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]        # 1,5
# g = ["A","A","A","B","B"]   # 3,4
# g = ["A"]       # 1,1
g = ["A","B","B","B","B","B","B","C","B","A"]       # 8,10

print(solution(g))