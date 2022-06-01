def fibonacci(n):

    """

    The fibonacci function takes in a one argument 
    (n) and return the nth value of fibonacci series

    0, 1, 1, 2, 3, 5, 8, 13, ..

    fibonacci formula is:

    fibonacci(n-1) + fibonacci(n-2)
    where n of 0 = 0 and n of 1 = 1

    """
    if n == 1 or n == 0: 
        return n
    
    else: 
        return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):

    """
    
    The lucas function takes in a one argument 
    (n) and return the nth value of lucas numbers
    where n of 0 = 2 and n of 1 =  1.

    2, 1, 3, 4, 7, 11, 18, 29, ...

    lucas formula(n) is:

    lucas(n-1) + lucas(n-2)

    """
    
    if n == 1:
        return 1
    elif n == 0:
        return 2
    
    else: 
        return lucas(n-1) + lucas(n-2)

def sum_series(n, option1 = 0, option2 = 1 ):
    
    """
    
    The sum_series function takes in a one required argument 
    (n) and two optional arguments given default values of 0 and 1 and return the nth value of lucas numbers or other series
    where n of 0 = option1 and n of 1 =  option.

    option1, option2, (n-1)+(n-2) + ..........

    lucas formula(n) is:

    lucas(n-1) + lucas(n-2)

    """

    
    if n == 0: return option1
    elif n == 1: return option2
    else: 
        # return sum_series(n-1, option1 = option1, option2 = option2) + sum_series(n-2, option1 = option1, option2 = option2)
        return sum_series(n-1, option1, option2) + sum_series(n-2, option1, option2)
    # no need to have option1 = option1 ad option2 = option2. 
    # just put option1 and option2