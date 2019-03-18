"""This problem was asked by Palantir.

Write an algorithm to justify text. Given a sequence of words and an integer line length k, return a list of strings which represents each line, fully justified.

More specifically, you should have as many words as possible in each line. There should be at least one space between each word. Pad extra spaces when necessary so that each line has exactly length k. Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.

If you can only fit one word on a line, then you should pad the right-hand side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16, you should return the following:

["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly

"""

from functools import reduce
def padSpace(stringlist, numK):
    if len(stringlist) == 1:
        return stringlist[0].ljust(numK)
    total = len(''.join(stringlist))
    
    spaceAll = int((numK-total)/(len(stringlist)-1))
    spaceMod = (numK-total)%(len(stringlist)-1)
    for i in range(len(stringlist)):
        if i != (len(stringlist)-1):
            if spaceMod >0:
                stringlist[i]=stringlist[i].ljust(spaceAll +1+len(stringlist[i]))
                spaceMod = spaceMod -1
                
            else:
                stringlist[i]=stringlist[i].ljust(spaceAll+len(stringlist[i]))
                
        else:
            return (''.join(stringlist))
    
def spaceMatch(stringlist, numK):
    strlen = 0
    index=0
    returnStr=[]
    for i in range(len(stringlist)):
        if (strlen+len(stringlist[i])) == numK:
            returnStr.append(' '.join(stringlist[index:i+1]))
            strlen =0
            index = i+1
        elif (strlen+len(stringlist[i])) > numK:
            strlen = len(stringlist[i])+1
            returnStr.append(padSpace(stringlist[index:i], numK))
            index = i
        elif i == len(stringlist) -1:
            returnStr.append(padSpace(stringlist[index:], numK))
        else:
            strlen = strlen + len(stringlist[i]) +1
            
            
    return returnStr

inputString=["the", "quick","brown", "fox", "jumps", "over", "the", "lazy", "dog"]
print(spaceMatch(inputString,16))
                 