def solution(w,h):
    
    if w<h:
        temp = w
        w = h
        h = temp
    
    a = h/w

    lost = 0
    last = 0
    now = 0
    for i in range(1,w+1):
        now = i*a
        if now - int(now) == 0:
            lost += 1
        elif int(now) > int(last):
            lost += 2
        else:
            lost += 1
        last = now

    return w*h - lost

print(solution(8,12))