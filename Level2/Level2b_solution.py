def answer(n, b):
    def subtraction(str1, str2, base, resid):
        '''generate subtraction results of two number strings
        with base using recursion'''
        if len(str1) == 0:
            return ''
        # process substraction of the last digit 
        elif int(str1[-1]) - resid >= int(str2[-1]):
            return subtraction(str1[:-1], str2[:-1], base, 0)\
            + str(int(str1[-1]) - int(str2[-1]) - resid)
        else:
            return subtraction(str1[:-1], str2[:-1], base, 1)\
            + str(int(str1[-1]) - int(str2[-1]) - resid + base)
    # initiate a queue of strings
    queue = [n]
    while True:
        # sort the string to generate x and y
        y = ''.join(sorted(n))
        x = y[::-1]
        # process the subtraction
        z = subtraction(x, y, b, 0)
        # check if z already in the queue
        if z in queue:
            return len(queue) - queue.index(z)
        else:
            queue.append(z)
            n = z
