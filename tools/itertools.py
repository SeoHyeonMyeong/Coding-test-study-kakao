from itertools import (product,
                       permutations,
                       combinations,
                       combinations_with_replacement,
                       accumulate,
                       groupby,)

# 내적
def product_test():
    a = [1, 2]
    b = [3, 4]
    prod = product(a,b, repeat=1)
    print(list(prod))
    
    return

# 순열
def permutations_test():
    a = [1, 2, 3]
    perm = permutations(a)
    print(list(perm))
    
    return

# 조합
def combinations_test():
    a = [1, 2, 3, 4]
    comb = combinations(a)
    comb_r = combinations_with_replacement(a)
    print(list(comb))
    print(list(comb_r))

    return

# 축적
def accumulate_test():
    a = [1, 2, 5, 3, 4]
    acc = accumulate(a, func=max)
    print(list(acc))
    
    return

# 그룹화
def gruopby_test():
    a = [1, 2, 3, 4]
    groupby_obj = groupby(a, key=lambda x: x<3)
    for key, value in groupby_obj:
        print(key, list(value))


if __name__ == "__main__":
    # product_test()
    # permutations_test()
    # combinations_test()
    # accumulate_test()
    gruopby_test()