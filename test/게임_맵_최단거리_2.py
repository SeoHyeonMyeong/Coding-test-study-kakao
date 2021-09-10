from collections import deque
import copy

map_ = []

def next_step(p):
    global map_

    n = len(map_)
    m = len(map_[0])

    next_point = deque()
    dirs = [[0,1],[0,-1],[1,0],[-1,0]]

    for d in dirs:
        if 0 <= p[0] + d[0] < n and 0 <= p[1] + d[1] < m:
            new_p = [p[0]+d[0], p[1]+d[1]]
            if map_[new_p[0]][new_p[1]] == 1:
                next_point.append(new_p)
    return next_point

def solution(maps):
    global map_

    map_ = copy.deepcopy(maps)
    n = len(maps)
    m = len(maps[0])

    begin = [0,0]
    map_[0][0] = 0
    end = [n-1,m-1]

    q = deque([[begin,1]])
    
    while q:
        current,count = q.popleft()

        if current == end:
            return count
        
        next_q = next_step(current)
        for item in next_q:
            q.append([item,count+1])
            map_[item[0]][item[1]] = 0
    return -1

maps = [
    [1,0,1,1,1],
    [1,0,1,0,1],
    [1,0,1,1,1],
    [1,1,1,0,1],
    [0,0,0,0,1],
    [0,1,1,1,1]
]

# my_way = Way([3,2],[-1,0],3)
# my_way.move(maps)
# for way in open_way:
#     way.show()
print(solution(maps))
