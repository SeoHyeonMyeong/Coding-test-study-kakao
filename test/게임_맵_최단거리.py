import copy

open_way = []
all_dir = [
    [0,1],
    [0,-1],
    [1,0],
    [-1,0]
]
map_ = []

class Way:
    coord = [0,0]
    open_direction = [0,0]
    distance = 0

    def __init__(self,coord,dir,dis):
        self.coord = coord
        self.open_direction = dir
        self.distance = dis
    
    def move(self):
        global all_dir
        global open_way
        global map_
        n_row = len(map_)
        n_col = len(map_[0])
        # map_[self.coord[0]][self.coord[1]] = 0
        self.coord[0] += self.open_direction[0]
        self.coord[1] += self.open_direction[1]
        if map_[self.coord[0]][self.coord[1]] == 0:
            return
        self.distance += 1
        dir = all_dir.copy()
        dir.remove([-self.open_direction[0],-self.open_direction[1]])
        
        if self.coord[0] == 0:
            dir.remove([-1,0])
        elif map_[self.coord[0]-1][self.coord[1]] == 0:
            if [-1,0] in dir:
                dir.remove([-1,0])
        
        if self.coord[0] == n_row-1:
            dir.remove([1,0])
        elif map_[self.coord[0]+1][self.coord[1]] == 0:
            if [1,0] in dir:
                dir.remove([1,0])

        if self.coord[1] == 0:
            dir.remove([0,-1])
        elif map_[self.coord[0]][self.coord[1]-1] == 0:
            if [0,-1] in dir:
                dir.remove([0,-1])
        
        if self.coord[1] == n_col-1:
            dir.remove([0,1])
        elif map_[self.coord[0]][self.coord[1]+1] == 0:
            if [0,1] in dir:
                dir.remove([0,1])

        if len(dir)>=2:
            map_[self.coord[0]][self.coord[1]] = 1
        else:
            map_[self.coord[0]][self.coord[1]] = 0
        for d in dir:
            new_way = Way(self.coord.copy(),d,self.distance)
            open_way.append(new_way)
        return

    def show(self):
        print(self.coord,self.open_direction,self.distance)

def solution(maps):
    global map_
    map_ = copy.deepcopy(maps)
    ans = []
    n_row = len(map_)
    n_col = len(map_[0])

    init_coord = [n_row-1,n_col-1]
    init_dis = 0
    init_way_1 = Way(init_coord.copy(),[-1,0],init_dis)
    init_way_2 = Way(init_coord.copy(),[0,-1],init_dis)
    if not map_[n_row-2][n_col-1] == 0:
        open_way.append(init_way_1)
    if not map_[n_row-1][n_col-2] == 0:
        open_way.append(init_way_2)
    map_[n_row-1][n_col-1] = 0
    while len(open_way) != 0:
        way = open_way.pop(0)
        # way.show()
        if way.coord == [1,0] or way.coord == [0,1]:
            return way.distance +2
            ans.append(way.distance + 2)
        else:
            way.move()
    
    if len(ans) == 0:
        return -1
    return min(ans)

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
