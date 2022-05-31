from functools import reduce

def lambda_test():
    add10 = lambda x: x + 10
    print("using lambda function add10 : ", add10(10))
    
    mult = lambda x,y: x * y
    print("using lambda function mult : ", mult(2,5))
    
    return

def lambda_sort_test():
    points = [(1, 2), (15, 1), (5, -1), (10, 4), (1, 5)]
    points_sorted = sorted(points, key=lambda x: x[1])
    print(points)
    print(points_sorted)

    return
    
def lambda_map_test():
    a = [1, 2, 3, 4, 5]
    b = list(map(lambda x: x*2, a))
    c = [x * 2 for x in a]
    print(a)
    print(b)
    print(c)
    
    return

def lambda_filter_test():
    a = [1, 2, 3, 4, 5, 6]
    b = list(filter(lambda x: x%2==0, a))
    c = [x for x in a if x%2==0]
    print(a)
    print(b)
    print(c)
    
    return

def lambda_reduce_test():
    a = [1, 2, 3, 4]
    
    product_a = reduce(lambda x,y: x*y, a)
    print(a)
    print(product_a)
    
    return
    
    
if __name__ == "__main__":
    # lambda_test()
    # lambda_sort_test()
    # lambda_map_test()
    lambda_filter_test()
    lambda_reduce_test()