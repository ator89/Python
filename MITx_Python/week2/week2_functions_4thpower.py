def fourthPower(x):
    '''
    x: int or float.
    '''
    # Your code here
    def square(x):
        return pow(x,2)
    val = pow(square(x),2)
    return val