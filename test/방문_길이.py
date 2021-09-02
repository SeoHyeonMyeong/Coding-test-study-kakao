
roads = []
coord = [0,0]

def move(direction):
    global roads
    global coord
    new_coord = coord.copy()
    if direction =="L" and coord[0] > -5:
        new_coord[0] -= 1
    elif direction =="R" and coord[0] < 5:
        new_coord[0] += 1
    elif direction =="U" and coord[1] < 5:
        new_coord[1] += 1
    elif direction =="D" and coord[1] > -5:
        new_coord[1] -= 1
    else:
        return
        
    road = [coord, new_coord]
    road.sort(key=lambda x:(x[0],x[1]))
    if not road in roads:
        roads.append(road)
    coord = new_coord

def solution(dirs):
    global coord
    global roads
    for d in dirs:
        move(d)
    return len(roads)
