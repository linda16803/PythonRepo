"""This problem was asked by Microsoft.

Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
"""




def findWord(wordList,inputString):
    index = 0
    returnWord=[]
    for x in range(len(inputString)):
        if inputString[index:x+1] in wordList:
            returnWord.append(inputString[index:x+1])
            index = x + 1
    if index < len(inputString): return None
    return returnWord
       
inputString ="thequickbedbathand"
wordList=["brown","bed","bath","bedbath","and","beyond","the","quick","fox"]
print(findWord(wordList,inputString))
