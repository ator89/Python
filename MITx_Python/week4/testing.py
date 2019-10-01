VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2,
    'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1,
    'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1,
    'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}


def getWordScore(word, n):

    suma = 0
    score = 0

    for key in SCRABBLE_LETTER_VALUES:
        for x in word:
            if key == x:
                suma += SCRABBLE_LETTER_VALUES[key]

    score = suma * len(word)
    if n == len(word):
        score += 50

    return score

print(getWordScore('aaa',3))


def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    handOrig = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    handCopy = handOrig.copy()
    word = "hello"

    for key in handOrig:
        for letter in word:
            if key == letter:
                del handCopy[key]

    return handCopy



sequence = 'mipalabra'
freq = {}
for x in sequence:
    freq[x] = freq.get(x, 0) + 1

#print(freq)



handOrig = {'h': 1, 'e': 1, 'l': 2, 'o': 1, 't': 3}
handCopy = handOrig.copy()
word = "hello"



for letter in word:
    handCopy[letter] -= 1
    if handCopy[letter] == 0:
        del handCopy[letter]
#print(handCopy)

def playHand(hand, wordList, n):
    pass

def displayHand(hand):
    t = ""
    for letter in handOrig.keys():
        for j in range(handOrig[letter]):
            #print(letter, end=" ")       # print all on the same line
            t += letter + " "
    return t
    #print()
print("\n")

t = displayHand(handOrig)

#ttt = {}
#ttt = displayHand(handOrig)

print(t)
option = input("Enter n to deal a new hand, r to replay the last hand, or e to end game:")

