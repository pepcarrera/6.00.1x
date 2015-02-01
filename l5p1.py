def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    result = 1.0
    while exp >= 1:
        result = result * base
        exp -= 1
    return result
