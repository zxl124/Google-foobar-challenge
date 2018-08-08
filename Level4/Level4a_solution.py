def answer(num_buns, num_required):
    # each key has to appear at least num_buns-num_required+1 times
    # otherwise, there will be combinations of bunnies who don't have the key
    # let key_min = num_buns-num_required+1
    # there are C(num_buns, key_min) ways of distribution for each key
    # assign a different key to every combination, it is the solution
    # because if any of the combination is missing,
    # one can simply pick the complement of that combination,
    # that combination of num_required-1 bunnies will have all the keys
    # thus violate the problem requirement
    from itertools import combinations
    # initialize an empty list of lists
    solution = [[] for i in range(num_buns)]
    # generate the combinations of bunnies
    bun_combs = combinations(range(num_buns), num_buns-num_required+1)
    # get the number of keys
    for key, bunnies in enumerate(bun_combs):
        for bunny in bunnies:
            solution[bunny].append(key)
    return solution
