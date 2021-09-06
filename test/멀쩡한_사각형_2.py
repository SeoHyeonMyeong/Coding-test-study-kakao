def solution(w,h):
    
    square = w*h
    lost = w+h

    gcd = 0
    for i in range(1, h+1):
        if w % i ==0 and h % i ==0:
            gcd = i
    return square - lost + gcd

print(solution(8,12))