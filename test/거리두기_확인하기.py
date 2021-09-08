distance = 5

class Person:
    coord = [0,0]
    wall =[0,0,0,0]

    def __init__(self,coord,wall):
        # coord [row,col]
        self.coord = coord
        # wall [left, right, up, down]
        self.wall = wall
    
    def show(self):
        print("좌표: [%d,%d]"%(self.coord[0],self.coord[1]))
        print("벽: 좌%d, 우%d, 상%d 하%d"%(self.wall[0],self.wall[1],self.wall[2],self.wall[3]))

    def is_fine(self,other):
        diff, x_dir, y_dir = self.diff_direction(other.coord)
        if diff > 2:
            return True
        if diff < 2:
            return False
        y_fine = False
        x_fine = False
        
        y_con_1 = y_dir == 0
        # 아래쪽에 벽이 있는지
        y_con_2 = y_dir == 1 and self.wall[3] == 1
        # 위쪽에 벽이 있는지
        y_con_3 = y_dir == -1 and self.wall[2] == 1
        if y_con_1 or y_con_2 or y_con_3:
            y_fine = True
        

        x_con_1 = x_dir == 0
        # 오른쪽에 벽이 있는지
        x_con_2 = x_dir == 1 and self.wall[1] == 1
        # 왼쪽에 벽이 있는지
        x_con_3 = x_dir == -1 and self.wall[0] == 1
        if x_con_1 or x_con_2 or x_con_3:
            x_fine = True

        if x_fine and y_fine:
            return True
        return False

    # 거리와 위치 측정
    def diff_direction(self,coord):
        y_diff = coord[0] - self.coord[0]
        x_diff = coord[1] - self.coord[1]
        if not x_diff == 0:
            x_dir = int(x_diff / abs(x_diff))
        else:
            x_dir = 0
        if not y_diff == 0:
            y_dir = int(y_diff / abs(y_diff))
        else:
            y_dir = 0
        diff = abs(x_diff) + abs(y_diff)
        return diff, x_dir, y_dir

def solution(places):
    ans = []
    for place in places:
        person = find_person(place)
        # 사람이 2명도 안되면 안전!
        if len(person) < 2:
            ans.append(1)
        else:
            isbreak = False
            for i in range(len(person)):
                for j in range(i+1,len(person)):
                    if not person[i].is_fine(person[j]):
                        ans.append(0)
                        isbreak=True
                        break
                if isbreak:
                    break
            if not isbreak:
                ans.append(1)
    return ans

def find_person(place):
    person = []
    for row in range(distance):
        for col in range(distance):
            if place[row][col] == "P":
                if col == 0:
                    left = 1
                elif place[row][col-1] =="X":
                    left = 1
                else:
                    left = 0
                
                if col == distance-1:
                    right = 1
                elif place[row][col+1] =="X":
                    right = 1
                else:
                    right = 0

                if row == 0:
                    up = 1
                elif place[row-1][col] =="X":
                    up = 1
                else:
                    up = 0
                
                if row == distance-1:
                    down = 1
                elif place[row+1][col] =="X":
                    down = 1
                else:
                    down = 0
                new_person = Person([row,col],[left,right,up,down])
                person.append(new_person)
    return person

print(solution([["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"]]))