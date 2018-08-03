def answer(n):
    # for even numbers: answer(n) = answer(n/2) + 1
    # for odd numbers: answer(n) = min(answer(n+1), answer(n-1)) + 1
    # we can find out answer(n) by using recursion
    # however, we can do this quicker by doing some math beforehand
    # for n = 4m+1 or 4m-1, the shortest path to m is through 4m and 2m
    # therfore the entire strategy should be moving to multiples of 4 for odd
    # numbers, and division by 2 for even numbers.
    
    # define answers for n < 4
    known_answers = {1:0, 2:1, 3:2}
    n = long(n)
    steps = 0
    # keeps transforming until it hit one of the three known answers
    while n not in known_answers:
        if n % 2 == 0:
            n = n / 2
        elif n % 4 == 1:
            n -= 1
        else:
            n += 1
        steps += 1
    # add known answers to previous steps
    return steps + known_answers[n]
