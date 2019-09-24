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


def hangman(secretWord):
    cantidadLetras = len(secretWord)
    mistakesMade = 0
    lettersGuessed = []

    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is', cantidadLetras, 'letters long.')
    ###

    while 8 - mistakesMade > 0:



        if isWordGuessed(secretWord, lettersGuessed) == True:
            print('----------')
            print('Congratulations, you won!')
            break
        else:
            print('----------')
            print('You have', 8 - mistakesMade, 'guesses left.')
            print('Available letters:', getAvailableLetters(lettersGuessed))
            letter = input('Please guess a letter: ').lower()

            if letter in secretWord and letter not in lettersGuessed:
                lettersGuessed.append(letter)
                print('Good guess:', getGuessedWord(secretWord, lettersGuessed))
            elif letter in lettersGuessed:
                print("Oops! You've already guessed that letter:",getGuessedWord(secretWord, lettersGuessed ))
            elif letter not in secretWord:
                print('Oops! That letter is not in my word:',getGuessedWord(secretWord, lettersGuessed))
                lettersGuessed.append(letter)
                mistakesMade += 1

        if 8 - mistakesMade == 0:
            print('------------')
            print('Sorry, you ran out of guesses. The word was', secretWord)
            break
        else:
            continue

lil = ['z', 'x', 'q', 'b', 'r', 'o', 'c', 'c', 'o', 'l', 'i','a','4','e','l']

#print(isWordGuessed('apple',lil))
#print(getGuessedWord('ad',lil))
print(getAvailableLetters('asd'))

hangman('hola')