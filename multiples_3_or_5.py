def multiples_3_or_5(number):
    '''Add all the numbers multiples of 3 or 5 in a determined range'''
    result = 0

    for x in range(number):
       if x % 3 == 0 or x % 5 == 0:
            result += x
        
    return result 

