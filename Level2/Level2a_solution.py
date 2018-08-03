def answer(pegs):
    from fractions import Fraction
    # the radius of the first peg when there are an even number of positions should be
    # 2/3 * (-X[0]+X[-1]+2X[odd]-2X[even])
    # odd being odd indices, even being even indices, except first and last
    # the radius of the first peg when there are an odd number of positions whould be
    # 2 * (-X[0]-X[-1]+2X[odd]-2X[even])
    result = -pegs[0]
    for i in range(1, len(pegs)-1):
        if i % 2 == 0:
            result -= 2 * pegs[i]
        else:
            result += 2 * pegs[i]
    if len(pegs) % 2 == 0:
        result += pegs[-1]
        result = Fraction(2 * result, 3)
    else:
        result -= pegs[-1]
        result = result * 2
    # every gear must have radius >= 1, check for that
    if result < 1:
        return [-1, -1]
    gear = result
    flag = True
    for i in range(1, len(pegs)):
        if pegs[i] - pegs[i-1] - gear < 1:
            flag = False
            break
    if flag:
        return [result.numerator, result.denominator]
    else:
        return [-1, -1]
