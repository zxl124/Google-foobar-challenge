def answer(g):
    from collections import defaultdict
    n_row = len(g)+1
    n_col = len(g[0])+1
    # make a collection of all possible binary combinations per column
    col_combination = dict()
    for i in range(2**n_row):
        # convert int to binary, then to list, stored in dict with int as key
        col_combination[i] = [int(j) for j in bin(i)[2:].zfill(n_row)]

    # transpose g
    g_transpose = list(zip(*g))
    # transform binary array into int to make comparisons faster
    g_transpose = [int(''.join(str(int(j)) for j in i), 2) for i in g_transpose]

    # define a function to covert two columns into T/F as defined by the problem
    def transform(col1, col2):
        result = list()
        for i in range(len(col1)-1):
            result.append(
                sum((col1[i], col1[i+1], col2[i], col2[i+1])) == 1)
        # convert the binary array to make comaprisons faster
        result = int(''.join(str(int(i)) for i in result), 2)
        return result
    
    # calculate transformations of all combinatinos of rows and store them
    # also storm possible combinations
    transformations = dict()
    combinations = defaultdict(list)
    for i in range(2**n_row):
        for j in range(2**n_row):
            result = transform(col_combination[i], col_combination[j])
            if result in g_transpose:
                transformations[(i,j)] = result
                combinations[i].append(j)
                
    # find all combinations of columns 1 and 2 that would transform into
    # the first column of g
    count_left = {i:1 for i in range(2**n_row)}
    col_left = combinations.keys()
    n = 2
    while n <= n_col:
        count_right = defaultdict(int)
        for i in col_left:
            for j in combinations[i]:
                if transformations[(i,j)] == g_transpose[n-2]:
                    count_right[j] += count_left[i]
        n += 1
        count_left = count_right.copy()
        col_left = list(count_left.keys())
    return sum(count_right.values())

g = [[True, True, False, True, False, True, False, True, True, False], [True, True, False, False, False, False, True, True, True, False], [True, True, False, False, False, False, False, False, False, True], [False, True, False, False, False, False, True, True, False, False]]

print(answer(g))
