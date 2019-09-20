def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    myDict = {}
    count = 0
    for word in aDict.values():
        # if word in dict, increase

        count += len(word)

    return count