def answer(start, length):
    # define a function f(n) to calculate 1^2^3^...^n
    # because 4m+3 ^ 4m+2 = 1 and 4m+1 ^ 4m = 1
    # 4m+3 ^ 4m+2 ^ 4m+1 ^ 4m = 0
    # therefore f(4m+3) = f(3) = 0
    # f(4m+2) = f(4m+3) ^ 4m+3 = 0 ^ 4m+3 = 4m+3
    # f(4m+1) = f(4m+2) ^ 4m+2 = 4m+3 ^ 4m+2 = 1
    # f(4m) = f(4m+1) ^ 4m+1 = 1 ^ 4m+1 = 4m
    def xor_one_to_n(n):
        if n % 4 == 0:
            return n
        elif n % 4 == 1:
            return 1
        elif n % 4 == 2:
            return n + 1
        else:
            return 0
    # define a function to calculate result for each row
    def row_answer(row_start, row_end):
        if row_start == row_end:
            return row_start
        else:
            return xor_one_to_n(row_end) ^ xor_one_to_n(row_start-1)
    # calculate results for all rows, and XOR together
    total = 0
    queue_start, queue_len = start, length
    while queue_len:
        total = total ^ row_answer(queue_start, queue_start+queue_len-1)
        queue_start += length
        queue_len -= 1
    return total
