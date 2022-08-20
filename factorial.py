def factorial(number):
    '''Calculate the factorial of a number'''
    result = 1

    for i in range(number):
        result *= i + 1

    return result
