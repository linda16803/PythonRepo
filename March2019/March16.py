"""
This problem was asked by Facebook.

Given a string of round, curly, and square open and closing brackets, 
return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.
"""


def balanceCheck(inputString):
    leftRound = leftCurly = leftSquare = 0
    
    for x in inputString:
        if x == '(': leftRound += 1      
        if x == '{': leftCurly += 1
        if x == '[': leftSquare += 1
        if x == ')': leftRound -= 1
        if x == '}': leftCurly -= 1
        if x == ']': leftSquare -= 1
        if leftRound < 0 or leftCurly < 0 or leftSquare < 0: return False
        
    if leftRound != 0 or leftCurly != 0 or leftSquare != 0: return False
    
    return True
    
    
print(balanceCheck("([][])[]({})"))
print(balanceCheck("([}])"))
print(balanceCheck("((())))("))