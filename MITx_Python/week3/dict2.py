def lyrics_to_frequencies(lyrics):
    myDict = {}
    for word in lyrics:
        #if word in dict, increase
        if word in myDict:
            myDict[word] += 1
        #assign ocurrence
        else:
            myDict[word] = 1
    return myDict


