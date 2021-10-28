class Block:
    row = 0
    col = 0
    def __init__(self,dir,pos):
        self.dir = dir
        self.pos = pos
        self.arr = [0,0,0,0]

    def __repr__(self):
        return str(self.arr) + self.dir + str(self.pos)

    def get_path(self):
        if self.arr[0] == 0:
            self.arr[0] = 1
            return "U"
        elif self.arr[1] == 0:
            self.arr[1] = 1
            return "D"
        elif self.arr[2] == 0:
            self.arr[2] = 1
            return "L"
        elif self.arr[3] == 0:
            self.arr[3] = 1
            return "R"
        return False

    def get_path(self):
        if self.arr[0] == 0:
            self.arr[0] = 1
            return "U"
        elif self.arr[1] == 0:
            self.arr[1] = 1
            return "D"
        elif self.arr[2] == 0:
            self.arr[2] = 1
            return "L"
        elif self.arr[3] == 0:
            self.arr[3] = 1
            return "R"
        return False

    def get_pos(self):
        return self.pos
    
    def next(self,d):
        if d == "U":
            if self.pos[0] == 0:
                return Block.row - 1, self.pos[1]
            return self.pos[0] - 1, self.pos[1]
        elif d == "D":
            if self.pos[0] == Block.row - 1:
                return 0, self.pos[1]
            return self.pos[0] + 1, self.pos[1]
        elif d == "L":
            if self.pos[1] == 0:
                return self.pos[0], Block.col - 1
            return self.pos[0], self.pos[1] - 1
        elif d == "R":
            if self.pos[1] == Block.col - 1:
                return self.pos[0], 0
            return self.pos[0], self.pos[1] + 1

    def get_rotation(self, f):
        if self.dir == "S":
            key = f
        elif self.dir == "L":
            key = {"U":"L", "D":"R", "L":"D", "R":"U"}.get(f)
        elif self.dir == "R":
            key = {"U":"R", "D":"L", "L":"U", "R":"D"}.get(f)
        
        if key == "U":
            self.arr[0] = 1
        elif key == "D":
            self.arr[1] = 1
        elif key == "L":
            self.arr[2] = 1
        elif key == "R":
            self.arr[3] = 1
        return key

def solution(grid):
    ans = []
    result = []
    
    Block.row = len(grid)
    Block.col = len(grid[0])

    for i in range(len(grid)):
        line = []
        for j in range(len(grid[i])):
            line.append(Block(grid[i][j],[i,j]))
        ans.append(line)

    for line in ans:
        for block in line:
            while block.arr != [1,1,1,1]:
                i,j = block.get_pos()
                d = block.get_path()
                count = 1
                if not d:
                    continue

                x,y = block.next(d)
                new_block = ans[x][y]
                new_dir = new_block.get_rotation(d)
                
                while [x,y,new_dir] != [i,j,d]:
                    x,y = new_block.next(new_dir)
                    new_block = ans[x][y]
                    new_dir = new_block.get_rotation(new_dir)
                    count +=1
                result.append(count)

    result.sort()
    return result


grid = ["SL","LR"]
print(solution(grid))
