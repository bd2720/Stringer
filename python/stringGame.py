abc = "abcdefghijklmnopqrstuvwxyz"

# reverse a string
def rev(s, args):
  return s[::-1]

# add character at index i
def charAdd (s, args):
    i = args[0]
    i -= 1
    return s[:i] + s[i] + s[i:]

# remove character at index i
def charRem(s, args):
    i = args[0]
    i -= 1
    if i == -1:
        return s[:-1]
    return s[:i] + s[i+1:]

# inc/dec a char at index i by amount x (wraps)
def charChange(s, args):
    i = args[0]
    x = args[1]
    i -= 1
    letterVal = abc.index(s[i])
    letterVal = (letterVal + x) % 26
    return s[:i] + abc[letterVal] + s[i+1:]

# swap chars in a string
def swp(s, args):
    i = args[0]
    j = args[1]
    i -= 1
    j -= 1
    if i == j:
        return s
    elif i > j:
        i, j = j, i
    return s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]

# shift string right by amount x (wraps)
def shr(s, args):
    x = args[0]
    x = x % len(s)
    return s[-x:] + s[:-x]

# functionStringRep: (functionToCall, functionCost)
actionsDict = {
    "reverse": (rev, 3),
    "add": (charAdd, 3),
    "remove": (charRem, 2),
    "change": (charChange, 4),
    "swap": (swp, 1),
    "shift": (shr, 2)
}

# str1-->str2-->str3...
def stringSeq(strings):
    resStr = strings[0]
    for s in strings[1:]:
        resStr += "-->" + s
    return resStr

# list of (wordInital, wordFinal)
gamePairs = [
    ('pots', 'stop'),
    ('pots', 'spot'),
    ('plains', 'snail'),
    ('sever', 'verse')
]

## GAME LOOP ##
gameID = 2
currPair = gamePairs[gameID]
(wordInitial, wordFinal) = currPair
wordCurr = wordInitial
cost = 0
wordSeq = [wordInitial]
print("Target word: " + wordFinal)
while wordFinal != wordCurr:
    print("Cost: " + str(cost))
    print("Current word: " + wordCurr)
    actionInput = input("Enter an action: ")
    if actionInput == "exit": exit()
    actionInput = actionInput.split(" ")
    chosenAction = actionInput[0]
    # arguments
    actionArgs = [int(a) for a in actionInput[1:]]
    wordCurr = actionsDict[chosenAction][0](wordCurr, actionArgs)
    cost += actionsDict[chosenAction][1]
    wordSeq.append(wordCurr)

print("You win! Cost: " + str(cost))
print(stringSeq(wordSeq))