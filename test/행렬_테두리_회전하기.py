def solution(rows, columns, queries):
    table = []
    ans = []
    for i in range(rows):
        row = [*range(i*columns+1,(i+1)*columns+1)]
        table.append(row)
    for coord in queries:
        table,min_num = rotate(table,coord)
        ans.append(min_num)
    return ans


def rotate(table,coord):
    x_dir = 0
    y_dir = 1
    for i in range(len(coord)):
        coord[i] -= 1
    x1,y1,x2,y2 = coord
    x_diff = x2-x1
    y_diff = y2-y1
    x,y = x1,y1
    min = table[x][y]
    last = table[x][y]
    for i in range(x_diff*2 + y_diff *2):
        x += x_dir
        y += y_dir
        if table[x][y]< min:
            min = table[x][y]
        temp = table[x][y]
        table[x][y] = last
        last = temp
        if x == x1 and y == y2:
            x_dir,y_dir = 1,0
        if x == x2 and y == y2:
            x_dir,y_dir = 0,-1
        if x == x2 and y == y1:
            x_dir,y_dir = -1,0
    return table,min

print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))