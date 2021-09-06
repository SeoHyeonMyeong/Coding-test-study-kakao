def solution(v):
    x = []
    y = []

    for coord in v:
        pos_x = coord[0]
        pos_y = coord[1]
        
        if pos_x in x:
            x.remove(pos_x)
        else:
            x.append(pos_x)
        
        if pos_y in y:
            y.remove(pos_y)
        else:
            y.append(pos_y)

    answer = [x[0],y[0]]
    return answer