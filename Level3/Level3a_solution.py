def answer(m):
    # return [1,1] if only one state
    if len(m)<2:
        return [1,1]
    from fractions import Fraction, gcd
    # matrix multiplicatin function
    def multiply(m1, m2):
        from itertools import starmap
        from operator import mul
        return [sum(starmap(mul, zip(m1, col))) for col in zip(*m2)]
    # function to covert matrix into probabilities (float)
    def transform_matrix(matrix):
        for i in range(len(matrix)):
            if sum(matrix[i]) > 0:
                row_sum = sum(matrix[i])
                matrix[i] = [float(j)/row_sum for j in matrix[i]]
            else:
                # covert terminal rows into 0s and 1
                terminal = [0.0] * len(matrix)
                terminal[i] = 1.0
                matrix[i] = terminal
        return(matrix)
    # find terminal states
    terminal = []
    for index,row in enumerate(m):
        if sum(row) == row[index]:
            terminal.append(index)
    # convert matrix
    m = transform_matrix(m)
    # initialize the probability vector
    prob = m[0]
    # keep calculating the dot product of prob and m, until the sum of
    # probabilities of all terminal states are very close to 1.
    prob_threshold = 1e-10
    sum_terminal_prob = sum(prob[i] for i in terminal)
    while sum_terminal_prob < 1 - prob_threshold:
        # matrix multiplication
        prob = multiply(prob, m)
        sum_terminal_prob = sum(prob[i] for i in terminal)
    # process output
    for i in terminal:
        prob[i] = Fraction(prob[i]).limit_denominator()
    # find least common multiple
    denominators = [prob[i].denominator for i in terminal]
    lcm = reduce(lambda x,y:x*y/gcd(x,y), denominators)
    numerators = [prob[i].numerator*lcm/prob[i].denominator for i in terminal]
    return numerators+[lcm]
