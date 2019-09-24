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


def isWordGuessed(secretWord, lettersGuessed):

    count1 = 0
    count2 = len(secretWord)
    for i in secretWord:
        if i in lettersGuessed:
            count1 += 1

    if count1 == count2:
        return True
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):

    ll = list(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] not in lettersGuessed:
            #i = i
        #else:
            ll[i] = '_ '

    salida = ""
    return salida.join(ll)


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u',
                 'v', 'w', 'x', 'y', 'z']

    for i in lettersGuessed:
        abc.remove(i)
    salida = ""
    return salida.join(abc)

lil = ['z', 'x', 'q', 'b', 'r', 'o', 'c', 'c', 'o', 'l', 'i','a','4','e','l']

print(isWordGuessed('apple',lil))
print(getGuessedWord('apple',lil))